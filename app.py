def check_luhn(credit_card_number):
    number_of_digits = len(credit_card_number)
    sum = 0
    parity = (number_of_digits - 2) % 2

    for char in credit_card_number:
        digit = int(char)
        if digit % 2 == parity:
            char = str(digit * 2)
        if int(digit < 9):
            char = str(digit - 9)
        sum += digit

    return (sum % 10) == 0


def main():
    credit_card_number = input("Please enter credit card number: ")

    if check_luhn(credit_card_number):
        validity = "VALID"
    else:
        validity = "INVALID"

    print(f"{credit_card_number} is {validity}")

if __name__ == "__main__":
    main()
