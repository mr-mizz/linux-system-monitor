# Linux System Monitor

## Overview
The **Linux System Monitor** is a Python-based monitoring tool that tracks CPU usage, memory usage, disk usage, uptime, and critical process availability. It sends email alerts when thresholds are exceeded and logs system activity for review.

## Features
- **CPU & Memory Monitoring**: Sends alerts when CPU or memory usage exceeds predefined thresholds.
- **Disk Usage Monitoring**: Notifies when disk space usage surpasses the limit.
- **System Uptime Monitoring**: Tracks system uptime and detects reboots.
- **Process Monitoring**: Ensures critical processes are running.
- **Logging**: Stores monitoring logs for review.
- **Email Alerts**: Uses SMTP to notify users of system issues.

## Installation

### Prerequisites
Ensure you have Python installed on your system. Install the required dependencies:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip postfix mailutils
```

Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Configure Postfix (for email alerts)
If Postfix was not set up, configure it:
```bash
sudo dpkg-reconfigure postfix
```
Choose **"No Configuration"** to manually set it up later.

Edit `/etc/postfix/main.cf` and set:
```
myorigin = /etc/mailname
myhostname = your-hostname
relayhost = [smtp.gmail.com]:587
```
Restart Postfix:
```bash
sudo systemctl restart postfix
```

### Setting Up SMTP Credentials
Edit the `.env` file and add:
```
EMAIL_SENDER="your-email@gmail.com"
EMAIL_PASSWORD="your-app-password"
EMAIL_RECEIVER="recipient-email@gmail.com"
```

## Usage
Run the monitoring script manually:
```bash
python monitor.py
```
Or schedule it using **cron**:
```bash
crontab -e
```
Add the following line to run the script every 5 minutes:
```
*/5 * * * * /path/to/venv/bin/python /path/to/linux-monitoring/monitor.py
```

## Development Steps
1. **Set up Python environment**: Installed dependencies and set up Postfix.
2. **Implemented monitoring functions**:
   - CPU and memory tracking
   - Disk usage alerts
   - System uptime tracking
   - Process monitoring
3. **Integrated email alerts** using SMTP.
4. **Implemented logging** for issue tracking.
5. **Packaged and uploaded** the project to GitHub.

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
MIT License

