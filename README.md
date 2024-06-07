# System Health Monitoring Script

This script monitors the health of a Linux system by checking CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds, the script sends an alert to the console and a log file.


### to run the script
```markdown
## Usage

To run the system health monitoring script, use the following command:

```sh
python system_health_monitor.py


#### Configuration

Explain the configuration options available in the script.

```markdown

## Configuration

You can configure the thresholds for CPU usage, memory usage, and disk usage by modifying the following variables in the `system_health_monitor.py` script:

```python
CPU_USAGE_THRESHOLD = 80.0
MEMORY_USAGE_THRESHOLD = 80.0  
DISK_USAGE_THRESHOLD = 80.0  

You can also change the monitoring interval by modifying the monitor_interval variable

### Log File (system_health.log) Output
saba_@LAPTOP-SJDP:~$ python3 system_health_monitor.py
2024-06-07 16:16:23,870 - INFO - CPU usage is normal: 0.0%
2024-06-07 16:16:23,870 - INFO - Memory usage is normal: 15.9%
2024-06-07 16:16:23,870 - INFO - Disk usage is normal: 0.6%
2024-06-07 16:16:23,871 - INFO - Number of running processes: 37

2024-06-07 16:17:24,933 - INFO - CPU usage is normal: 0.0%
2024-06-07 16:17:24,934 - INFO - Memory usage is normal: 15.9%
2024-06-07 16:17:24,934 - INFO - Disk usage is normal: 0.6%
2024-06-07 16:17:24,934 - INFO - Number of running processes: 37

2024-06-07 16:18:25,997 - INFO - CPU usage is normal: 0.2%
2024-06-07 16:18:25,998 - INFO - Memory usage is normal: 15.9%
2024-06-07 16:18:25,999 - INFO - Disk usage is normal: 0.6%
2024-06-07 16:18:25,999 - INFO - Number of running processes: 37

2024-06-07 16:19:27,056 - INFO - CPU usage is normal: 0.0%
2024-06-07 16:19:27,057 - INFO - Memory usage is normal: 15.8%
2024-06-07 16:19:27,057 - INFO - Disk usage is normal: 0.6%
2024-06-07 16:19:27,058 - INFO - Number of running processes: 37

2024-06-07 16:20:28,120 - INFO - CPU usage is normal: 0.1%
2024-06-07 16:20:28,121 - INFO - Memory usage is normal: 15.8%
2024-06-07 16:20:28,121 - INFO - Disk usage is normal: 0.6%
2024-06-07 16:20:28,122 - INFO - Number of running processes: 37
