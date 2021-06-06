def fullName(frist_name, last_name):
    firstName = frist_name
    lastName = last_name
    fullName = f"{firstName} {lastName}"
    # return print(f"Hell {fullName.title()}!")
    return fullName

if __name__ == '__main__':
    first_name = "albert"
    last_name = "einstein"
    full_name = fullName(first_name, last_name)

    print(f"Hello {full_name.title()},would you like to learn some Python today")
    print(f"Hello {full_name.upper()},would you like to learn some Python today")
    print(f"Hello {full_name.lower()},would you like to learn some Python today")
    print(f"Hello {full_name.strip()},would you like to learn some Python today")
    language = "A person who never made a mistake never tried anything new."
    print(f"{full_name.title()} once said, \"{language}\"")
    print(f"{full_name.title().strip()} once said,\"{language.title()}\" \r{full_name.title()} once said,\"{language}\"")

    print()
