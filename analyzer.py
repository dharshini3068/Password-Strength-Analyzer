import re
import random
import string

print("\n=== PASSWORD STRENGTH ANALYZER ===\n")

password = input("Enter password: ")

score = 0

# LENGTH CHECK
if len(password) >= 8:
    score += 1
else:
    print("⚠ Password too short (min 8 chars)")

# LOWERCASE CHECK
if re.search(r"[a-z]", password):
    score += 1
else:
    print("⚠ Add lowercase letters")

# UPPERCASE CHECK
if re.search(r"[A-Z]", password):
    score += 1
else:
    print("⚠ Add uppercase letters")

# NUMBER CHECK
if re.search(r"[0-9]", password):
    score += 1
else:
    print("⚠ Add numbers")

# SYMBOL CHECK
if re.search(r"[!@#$%^&*]", password):
    score += 1
else:
    print("⚠ Add special symbols")

# RESULT
print("\n--- RESULT ---")

if score <= 2:
    print("🔴 Weak Password")
elif score == 3 or score == 4:
    print("🟡 Medium Password")
else:
    print("🟢 Strong Password")

# SUGGESTION GENERATOR
print("\n--- Suggested Strong Password ---")

chars = string.ascii_letters + string.digits + "!@#$%^&*"
suggested = "".join(random.choice(chars) for _ in range(12))

print("👉", suggested)
