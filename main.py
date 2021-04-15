import random


def generator():
    lower = "qwertyuiopasdfghjklzxcvbnm"
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "1234567890"
    symbols = "!@#$%^&*()_."

    full = lower + upper + numbers + symbols

    length = 10
    password = "".join(random.sample(full, length))
    print(password)


if __name__ == "__main__":
    generator()
