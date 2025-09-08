import datetime
import csv

def log_attendance(emp_id, status):
    now = datetime.datetime.now()
    with open("attendance.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, status, now.strftime("%Y-%m-%d %H:%M:%S")])

# Example usage
log_attendance("EMP104", "IN")
