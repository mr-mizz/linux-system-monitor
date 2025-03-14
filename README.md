# Linux System Monitor

## 📌 Overview
The **Linux System Monitor** is a Python-based tool that monitors system health, including:
- **CPU usage**
- **Memory usage**
- **Disk usage**
- **System uptime**
- **Critical process monitoring**
- **Automatic email alerts** for high resource usage and system restarts

This project helps ensure the stability of Linux servers by detecting performance issues early.

---

## 🛠️ Installation

### Prerequisites
Ensure you have **Python 3** installed on your Linux machine.

```bash
sudo apt update && sudo apt install python3 python3-pip -y
```

### Clone the Repository
```bash
git clone https://github.com/mr-mizz/linux-system-monitor.git
cd linux-system-monitor
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Email Alerts
To enable email notifications, update `monitor.py` with your email credentials:

```python
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
EMAIL_RECEIVER = "recipient-email@gmail.com"
```
🔹 **Tip:** Use an App Password instead of your main email password for security.

---

## 🚀 Usage
Run the monitor script with:
```bash
python3 monitor.py
```

To run it in the background:
```bash
nohup python3 monitor.py &
```

To stop the script:
```bash
ps aux | grep monitor.py  # Find process ID (PID)
sudo kill <PID>
```

---

## 📊 Features
- ✅ **Real-time CPU, Memory, and Disk Monitoring**
- ✅ **Uptime Tracking**
- ✅ **Process Monitoring**
- ✅ **Reboot Detection**
- ✅ **Automated Email Alerts**

---

## 📝 License
This project is licensed under the [MIT License](LICENSE).

---

## 📢 Contributions
Contributions are welcome! Feel free to fork this repo and submit pull requests.

---

## 📩 Contact
For issues, open a GitHub issue or reach out via email.

