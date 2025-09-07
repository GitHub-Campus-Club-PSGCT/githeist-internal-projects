# TechSphere Corporation - OTP Simulation Script
# Harmless test for retry logic

import random

def get_otp():
    return random.randint(100000, 999999)

for i in range(5):
    print("Generated OTP:", get_otp())
