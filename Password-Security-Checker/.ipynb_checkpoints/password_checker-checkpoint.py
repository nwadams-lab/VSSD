#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import math

def load_common_passwords(filename="10k-most-common.txt"):

    common_passwords = set()
    with open(filename, "r") as file:
        for line in file:
            common_passwords.add(line.strip())

    return common_passwords

def is_common_password(password, common_passwords):
    if password.lower() in common_passwords:
        return True
    else:
        return False

COMMON_PASSWORDS = load_common_passwords()

def password_strength(password):

    # Dictionary called results that has different flags relating to the strength of a password
    results = {
        "length": len(password),
        "has_upper": False,
        "has_lower": False,
        "has_digits": False,
        "has_symbols": False,
        "is_common": False,
        "score": 0,
        "issues": []
    }

    # Checks length of password and gives score based on result.
    if len(password) >= 12:
        results["score"] += 5
    elif len(password) >= 8:
        results["score"] += 3
        results["issues"].append("Password should be at least 12 characters or longer!")
    elif len(password) < 8:
        results["score"] += 1
        results["issues"].append("Password is too short (minimum: 8, recommended: 12+).")

    # Checks if there are any uppercase letters
    if re.search(r"[A-Z]", password):
        results["score"] += 3
        results["has_upper"] = True
    else:
        results["issues"].append("Password does not contain any uppercase letters.")

    # Checks if there are any lowercase letters
    if re.search(r"[a-z]", password):
        results["score"] += 3
        results["has_lower"] = True
    else:
        results["issues"].append("Password does not contain any lowercase letters.")

    # Checks if there are any digits
    if re.search(r"[0-9]", password):
        results["score"] += 3
        results["has_digits"] = True
    else:
        results["issues"].append("Password does not contain any numbers.")

    # Checks if there are any special characters
    if re.search(r"[`~!@#$%^&*()_\-+=\[\]{}|;:',<.>/?\\]", password):
        results["score"] += 3
        results["has_symbols"] = True
    else:
        results["issues"].append("Password does not contain any symbols.")

    # Checks if password is in a list of common/breached passwords
    if is_common_password(password, COMMON_PASSWORDS):
        results["score"] = 0
        results["is_common"] = True
        results["issues"].append("Password is in a known list of common/breached passwords.")

    return results


print("=== Password Strength Checker ===")

password = input("Enter a password to test: ")
result = password_strength(password)

print("\n=== PASSWORD REPORT ===")

print(f"Score: {result['score']}/17")

if result["is_common"]:
    print("This password is a COMMON or BREACHED password. Change it NOW!")

print("\nIssues:")
for issue in result["issues"]:
    print(f"- {issue}")


# In[ ]:




