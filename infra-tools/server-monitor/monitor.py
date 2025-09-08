import psutil
import time

while True:
    cpu = psutil.cpu_percent(1)
    mem = psutil.virtual_memory().percent
    if cpu > 80 or mem > 85:
        print("ALERT: High usage detected")
    time.sleep(10)
