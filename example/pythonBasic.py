def print_name(frist_name, last_name):
    firstName = frist_name
    lastName = last_name
    fullName = f"{firstName} {lastName}"
    return print(f"Hell {fullName.title()}!")


if __name__ == '__main__':
    message = print_name("joe", "joo")
    print(message)
   # print(message.upper())
   # print(message.lower())
   # print(message.rstrip())
