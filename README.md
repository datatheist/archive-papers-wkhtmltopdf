# Archive Papers with WKHTMLTOPDF
### A script to automate webpage archiving
# archive-papers-wkhtmltopdf
<br>
<br>
This repo was inspired by Palewire. On attempt to setup Palewire with GitHub Actions, there was the need to authenticate with the OpenID Connect Protocol which (I think unnecessarily) complicated a simple task to bring up a script that is able to archive webpages and send them to a slack channel. The purpose of this script is just that and nothing more.
<br><br>

To make it work, make sure you either setup the secret variables in a `secrets.py`: `SLACK_WEBHOOK_URL, SLACK_AUTH, OUTPUT_DIR, INPUT_DIR` 
<br><br>

Or you do that very same procedure in your system variables.
<br>
# Setting Up System Variables

System variables, also known as environment variables, can be set up differently depending on the operating system. Here's how you can do it on MacOS, Linux, and Windows:

## MacOS and Linux

You can set environment variables in your shell's profile script. This could be `~/.bash_profile`, `~/.bashrc`, or `~/.zshrc` depending on your shell. Open the appropriate file in a text editor and add lines like these:

```bash
export SLACK_WEBHOOK_URL="your-slack-webhook-url"
export SLACK_AUTH="your-slack-auth"
export OUTPUT_DIR="your-output-dir"
export INPUT_DIR="your-input-dir"
```

Save the file, and then run source ~/.bash_profile (or whichever file you edited) to load the new variables. You can check that the variables were set correctly by running echo $SLACK_WEBHOOK_URL (and the other variable names).

## Windows

On Windows, you can set environment variables through the System Properties window.

Right-click on Computer on the desktop or in the Start menu, choose Properties.
Choose “Advanced system settings.”
Click the Environment Variables button.
Under “System Variables” click New.
Enter the variable name and value, and click OK.
For example, you would enter SLACK_WEBHOOK_URL as the variable name and your-slack-webhook-url as the variable value. Repeat this process for SLACK_AUTH, OUTPUT_DIR, and INPUT_DIR.

You can check that the variables were set correctly by opening a new command prompt window (old command prompt windows will not have the new variables) and running echo %SLACK_WEBHOOK_URL% (and the other variable names).

Please replace `"your-slack-webhook-url"`, `"your-slack-auth"`, `"your-output-dir"`, and `"your-input-dir"` with your actual values. Let me know if you have any questions! 😊

## Final Setup: Virtual Environment & Requirements.txt 

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (on Windows)
.\venv\Scripts\activate

# Activate the virtual environment (on Unix or MacOS)
source venv/bin/activate

# Install requirements from requirements.txt
pip install -r requirements.txt
