import csv

def check_duplicates(file):
    seen = set()
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            entry = (row[0], row[2])  # BadgeID + Location
            if entry in seen:
                print("Duplicate swipe found:", row)
            seen.add(entry)

check_duplicates("badge_logs.csv")
