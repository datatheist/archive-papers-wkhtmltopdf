import subprocess
import requests
from datetime import datetime
import time
import os
from secrets import *
import re

###### 
######
###### 
# INPUT_DIR, OUTPUT_DIR, SLACK_WEBHOOK_URL & SLACK_AUTH variables are all put into a separate secrets.py file. 
###### 
######
###### 

### Source: https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory

images = [f for f in os.listdir('.') if re.match(r'[0-9]+.*\.jpg', f)]

# Set the path to the CSV file
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
    for img in range(images):
        send_to_slack(f"{OUTPUT_DIR}/{img}.jpg", "#test-palewire-webhook")
    time.sleep(1)  # Add a delay to avoid potential issues with rapid execution


if __name__ == "__main__":
    main()
