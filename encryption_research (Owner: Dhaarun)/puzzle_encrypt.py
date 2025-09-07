# TechSphere Corporation - Research Prototype
# Puzzle Encrypt: ROT13 + Base64 toy encryption

import base64

def puzzle_encrypt(msg: str) -> str:
    rot13 = msg.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    ))
    return base64.b64encode(rot13.encode()).decode()

def puzzle_decrypt(msg: str) -> str:
    decoded = base64.b64decode(msg.encode()).decode()
    return decoded.translate(str.maketrans(
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ))

if __name__ == "__main__":
    test = "TreasuryKeys123!"
    enc = puzzle_encrypt(test)
    print("Encrypted:", enc)
    print("Decrypted:", puzzle_decrypt(enc))
