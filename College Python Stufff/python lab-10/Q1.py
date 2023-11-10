import re as r

password = input("Enter a password: ").strip().split(',')
for i in password:
    if r.search(r'[a-z]', i) and r.search(r'[A-Z]', i) and r.search(r'[0-9]', i) and r.search(r'[$#@]', i) and 6 <= len(i) <= 12:
        print(i)