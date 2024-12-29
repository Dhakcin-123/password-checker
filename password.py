import re

def checkpassword(password):
    score = 0
    if len(password) >= 8:
        score+=1
    else:
        print("Password must be atleast 8 characters long")
    if re.search(r"[A-Z]",password):
        score+=1
    else:
        print("Password must contain atleast 1 uppercase letter")
    if re.search(r"[a-z]",password):
        score+=1
    else:
        print("Password must contain atleast one lowercase letter")
    if re.search(r"[0-9]",password):
        score+=1
    else:
        print("Password must contain atleast one number")
    if re.search(r"[!@#$%^&*()?/><,.';:]",password):
        score+=1
    else:
        print("Password must contain atleast one special character")
    if score == 5:
        return "Strong password"
    elif 3<=score<5:
        return "Moderate password"
    else:
        return "Weak password"

user_password = input("Enter a password to check the strength: ")
strength = checkpassword(user_password)
print(f"Password strength: {strength}")