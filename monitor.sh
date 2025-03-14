#!/bin/bash

# Set thresholds
CPU_THRESHOLD=80.0
MEM_THRESHOLD=90.0
ALERT_EMAIL="myName@email.com"

# Get current timestamp
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

# Get CPU usage
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

# Get Memory usage
mem_usage=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')

# Get Disk usage
disk_usage=$(df -h / | awk 'NR==2 {print $5}')

# Create JSON log entry
json_log="{\"timestamp\": \"$timestamp\", \"cpu\": \"$cpu_usage\", \"memory\": \"$mem_usage\", \"disk\": \"$disk_usage\"}"

# Append to log file
echo $json_log >> system_monitor.json

# Check if CPU usage is above threshold
if (( $(echo "$cpu_usage > $CPU_THRESHOLD" | bc -l) )); then
    alert_msg="[$timestamp] ALERT: High CPU usage detected: ${cpu_usage}%"
    echo $alert_msg | mail -s "CPU Alert!" $ALERT_EMAIL
    echo $alert_msg | tee -a system_monitor.json
fi

# Check if Memory usage is above threshold
if (( $(echo "$mem_usage > $MEM_THRESHOLD" | bc -l) )); then
    alert_msg="[$timestamp] ALERT: High Memory usage detected: ${mem_usage}%"
    echo $alert_msg | mail -s "Memory Alert!" $ALERT_EMAIL
    echo $alert_msg | tee -a system_monitor.json
fi
#!/bin/bash

# Set thresholds
CPU_THRESHOLD=80.0
MEM_THRESHOLD=90.0

# Get current timestamp
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

# Get CPU usage
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

# Get Memory usage
mem_usage=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')

# Get Disk usage
disk_usage=$(df -h / | awk 'NR==2 {print $5}')

# Log the results
echo "[$timestamp] CPU: ${cpu_usage}% | Memory: ${mem_usage}% | Disk: ${disk_usage}" >> system_monitor.log

# Check if CPU usage is above threshold
if (( $(echo "$cpu_usage > $CPU_THRESHOLD" | bc -l) )); then
    echo "[$timestamp] ALERT: High CPU usage detected: ${cpu_usage}%" | tee -a system_monitor.log
fi

# Check if Memory usage is above threshold
if (( $(echo "$mem_usage > $MEM_THRESHOLD" | bc -l) )); then
    echo "[$timestamp] ALERT: High Memory usage detected: ${mem_usage}%" | tee -a system_monitor.log
fi
#!/bin/bash

# Get current timestamp
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

# Get CPU usage
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

# Get Memory usage
mem_usage=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')

# Get Disk usage
disk_usage=$(df -h / | awk 'NR==2 {print $5}')

# Print the results
echo "[$timestamp] CPU: ${cpu_usage}% | Memory: ${mem_usage}% | Disk: ${disk_usage}" >> system_monitor.log
