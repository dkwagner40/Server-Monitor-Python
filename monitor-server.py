import psutil
import time

def monitor_cpu_usage(interval=1):
    try:
        while True:
            # Get CPU usage
            cpu_usage = psutil.cpu_percent(interval=interval)

            # Print CPU usage
            print(f"CPU Usage: {cpu_usage}%")

    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_cpu_usage()