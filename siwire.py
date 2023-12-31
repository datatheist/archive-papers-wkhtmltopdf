import csv
import subprocess
import requests
from datetime import datetime
import time
import os
from secrets import *

###### 
######
###### 
# INPUT_DIR, OUTPUT_DIR, SLACK_WEBHOOK_URL & SLACK_AUTH variables are all put into a separate secrets.py file. 
###### 
######
###### 

# Set the path to the wkhtmltopdf executable
WKHTMLTOPDF_PATH = "wkhtmltopdf"

# Set the path to the CSV file
CSV_FILE = f"{INPUT_DIR}/sites.csv"

LOG_FILE = f"{OUTPUT_DIR}/error_log.txt"


def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")


def send_to_slack(file_path, channel):
    if not os.path.exists(file_path):
        log_message(f"File not found: {file_path}")
        print(file_path)
        return

    try:
        with open(file_path, "rb") as file_content:
            payload = {
                "channels": channel,
                "initial_comment": f"New screenshot from {file_path}",
            }
            files = {"file": file_content}
            headers = {"Authorization": f"{SLACK_AUTH}"}
            response = requests.post("https://slack.com/api/files.upload", headers=headers, data=payload, files=files)
            print(payload)

            if response.status_code != 200:
                log_message(f"Failed to send file to Slack. Status code: {response.status_code}")
            else:
                log_message("File sent successfully to Slack!")
    except PermissionError:
        log_message(f"Permission denied: {file_path}")


def main():
    with open(CSV_FILE, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row

        for row in csv_reader:
            twitter, url, name, location, timezone, country, language, bundle, wait, no_adguard = row

            # Generate the command for wkhtmltopdf
            command = [
                f"{WKHTMLTOPDF_PATH} \"{url}\" \"{OUTPUT_DIR}/{twitter}.pdf\"",
            ]


            log_message(f"Executing command: {' '.join(command)}")
            subprocess.run(command, shell=True)

            send_to_slack(f"{OUTPUT_DIR}/{twitter}.pdf", "#test-palewire-webhook")
            time.sleep(1)  # Add a delay to avoid potential issues with rapid execution
            


if __name__ == "__main__":
    main()
