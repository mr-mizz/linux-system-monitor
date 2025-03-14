#!/usr/bin/env python3

import psutil
import smtplib
import os
import time
import shutil
from email.mime.text import MIMEText

# Thresholds
CPU_THRESHOLD = 80.0
MEM_THRESHOLD = 70.0
DISK_THRESHOLD = 90.0  # Alert if disk usage exceeds 90%

# Critical Processes to Monitor
CRITICAL_PROCESSES = ["sshd", "cron", "syslog", "nginx", "apache2", "mysql", "postgres"]

# Email settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_RECEIVER = "jmuli866@gmail.com"
EMAIL_PASSWORD = "your-app-password"

# File paths
HEARTBEAT_FILE = "/tmp/heartbeat.log"
LAST_BOOT_FILE = "/tmp/last_boot.log"

# Function to send alert emails
def send_email(subject, message):
    """Send an email alert."""
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()

        print("✅ Email alert sent!")
    except Exception as e:
        print("❌ Failed to send email:", str(e))
# CPU & Memory Monitoring
def check_system():
    """Check CPU & Memory usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu_usage}%, Memory Usage: {mem_usage}%")

    if cpu_usage > CPU_THRESHOLD:
        send_email("⚠️ High CPU Usage Alert", f"CPU usage is at {cpu_usage}%!")

    if mem_usage > MEM_THRESHOLD:
        send_email("⚠️ High Memory Usage Alert", f"Memory usage is at {mem_usage}%!")


# Uptime Monitoring
def check_uptime():
    """Check system uptime and log it."""
    uptime_seconds = float(os.popen("awk '{print $1}' /proc/uptime").read().strip())
    uptime_hours = uptime_seconds / 3600

    print(f"✅ System Uptime: {uptime_hours:.2f} hours")


# Detect System Reboots
def detect_reboot():
    """Check if the system has restarted."""
    boot_time = float(os.popen("awk '{print $1}' /proc/uptime").read().strip())

    if os.path.exists(LAST_BOOT_FILE):
        with open(LAST_BOOT_FILE, "r") as f:
            last_boot = float(f.read().strip())

        if boot_time < last_boot:
            send_email("⚠️ System Restart Detected", f"System restarted! Current uptime: {boot_time / 60:.2f} minutes.")

    with open(LAST_BOOT_FILE, "w") as f:
        f.write(str(boot_time))

# Disk Usage Monitoring
def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    usage_percent = (used / total) * 100

    if usage_percent > DISK_THRESHOLD:
        send_email("⚠️ Disk Usage Alert", f"Disk usage is at {usage_percent:.2f}%. Consider freeing up space.")

    print(f"✅ Disk usage: {usage_percent:.2f}%")


# Update Heartbeat File
def update_heartbeat():
    try:
        with open(HEARTBEAT_FILE, "w") as f:
            f.write(str(time.time()))
        print("✅ Heartbeat updated.")
    except Exception as e:
        print(f"❌ Error updating heartbeat: {str(e)}")

# Process Monitoring
def check_processes():
    running_processes = [p.info['name'] for p in psutil.process_iter(['name'])]

    for process in CRITICAL_PROCESSES:
        if process not in running_processes:
            send_email(f"⚠️ Process Alert: {process} Stopped!", f"The critical process '{process}' is not running.")
            print(f"❌ {process} is NOT running!")
        else:
            print(f"✅ {process} is running.")


if __name__ == "__main__":
    check_system()
    check_uptime()
    detect_reboot()
    check_disk_usage()
    update_heartbeat()
    check_processes()  # NEW: Monitor critical processes
