import re

def extract_email_parts(email):
    # Регулярное выражение для разбора email
    pattern = r'(?P<username>[^@]+)@(?P<domain>.+)'
    match = re.match(pattern, email)
    
    if match:
        username = match.group('username')
        domain = match.group('domain')
        return username, domain
    else:
        return None, None

def main():
    email = input("Введите адрес электронной почты: ")
    username, domain = extract_email_parts(email)
    
    if username and domain:
        print(f"Имя пользователя: {username}")
        print(f"Доменное имя: {domain}")
    else:
        print("Ошибка: введен некорректный адрес электронной почты.")

if __name__ == "__main__":
    main()
