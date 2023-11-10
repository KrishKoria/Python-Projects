import re


def extract_username(email):
    match = re.match(r"([a-zA-Z]+)@([a-zA-Z]+)\.com", email)
    if match:
        username = match.group(1).capitalize()
        return username
    else:
        return None


email_address = input("Enter an email address: ")

result = extract_username(email_address)

if result:
    print(result)
else:
    print("Invalid email address format.")
