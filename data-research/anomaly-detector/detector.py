import numpy as np

def detect_outliers(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return [x for x in data if abs(x - mean) > 2 * std_dev]

transactions = [200, 220, 210, 215, 10000, 230]
print("Outliers:", detect_outliers(transactions))
