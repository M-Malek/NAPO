import secrets


def generate_password():
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    CHARS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    num_letters = secrets.choice(NUMBERS[1::])
    num_chars = secrets.choice(NUMBERS[1::])
    num_numbers = secrets.choice(NUMBERS[1::])

    chosen_letters = [secrets.choice(LETTERS) for i in range(num_letters)]
    chosen_chars = [secrets.choice(CHARS) for j in range(num_chars)]
    chosen_numbers = [str(secrets.choice(NUMBERS)) for k in range(num_numbers)]
    password_source = chosen_letters + chosen_chars + chosen_numbers

    generated_password = ""
    for n in range(len(password_source)):
        char = secrets.choice(password_source)
        generated_password += char
        password_source.remove(char)

    return generated_password


def data_pierwszego_dodania():
    pass


def data_ostatniej_aktualizacji():
    pass
