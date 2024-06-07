import psutil
import time
import logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("system_health.log"),
                              logging.StreamHandler()])
CPU_USAGE_THRESHOLD = 80.0
MEMORY_USAGE_THRESHOLD = 80.0
DISK_USAGE_THRESHOLD = 80.0
def check_cpu_usage(threshold):
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > threshold:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage is normal: {cpu_usage}%")
    return cpu_usage

def check_memory_usage(threshold):
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > threshold:
        logging.warning(f"High memory usage detected: {memory_usage}%")
    else:
        logging.info(f"Memory usage is normal: {memory_usage}%")
    return memory_usage

def check_disk_usage(threshold):
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > threshold:
        logging.warning(f"High disk usage detected: {disk_usage}%")
    else:
        logging.info(f"Disk usage is normal: {disk_usage}%")
    return disk_usage

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f"Number of running processes: {process_count}")
    return process_count

def monitor_system(interval):
    while True:
        check_cpu_usage(CPU_USAGE_THRESHOLD)
        check_memory_usage(MEMORY_USAGE_THRESHOLD)
        check_disk_usage(DISK_USAGE_THRESHOLD)
        check_running_processes()
        
        time.sleep(interval)

if __name__ == "__main__":
    monitor_interval = 60  # in seconds
    monitor_system(monitor_interval)
