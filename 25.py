import re


def password(passw):
    if len(passw) < 8:
        return False
    if not re.search(r'[A-Z]',passw):
        return False
    if not re.search(r'[a-z]',passw):
        return False
    if not re.search(r'\d',passw):
        return False
    if not re.search(r'[^\w\s]',passw):
        return False
    return True

passw = "Master#123"
print(password(passw))
