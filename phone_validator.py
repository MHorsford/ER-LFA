class PhoneNumberValidator:
    @staticmethod
    def is_valid_phone_number(phone: str) -> bool:
        # Verifica se o número está no formato "(xx) 9xxxx-xxxx"
        if phone.startswith("(") and phone[3] == ")" and phone[4] == " " and phone[5] == "9" and phone[10] == "-":
            return phone[1:3].isdigit() and phone[6:10].isdigit() and phone[11:].isdigit()

        # Verifica se o número está no formato "(xx) 9xxxxxxxx"
        elif phone.startswith("(") and phone[3] == ")" and phone[4] == " " and phone[5] == "9":
            return phone[1:3].isdigit() and phone[6:].isdigit()

        # Verifica se o número está no formato "xx 9xxxxxxxx"
        elif phone[2] == " " and phone[3] == "9":
            return phone[:2].isdigit() and phone[4:].isdigit()

        return False


if __name__ == "__main__":

    phones = [
        "(91) 99999-9999",  # Válido
        "(91) 999999999",  # Válido
        "91 999999999",  # Válido
        "(11) 91234-5678",  # Válido
        "(21) 98765-4321",  # Válido
        "11 987654321",  # Válido
        "(11) 9292929292",  # Válido
        "22 922222222",  # Válido

        "(91) 59999-9999",  # Inválido (quantidade incorreta de dígitos no número)
        "99 99999-9999",  # Inválido (não pode começar com 9 no DDD)
        "(94)95555-5555",  # Inválido (formato incorreto, falta espaço)
        "(55) 999999-8888",  # Inválido (quantidade incorreta de dígitos no número)
        "(11) 811111-1111",  # Inválido (não pode começar com 8)
        "(92) 9999-9999",  # Inválido (deve começar com 9)
        "(22) 909090-9090",  # Inválido (formato incorreto, falta o hífen)
    ]

    for phone in phones:
        is_valid = PhoneNumberValidator.is_valid_phone_number(phone)
        print(f"'{phone}': {"\033[92m" + 'Válido' + "\033[0m" if is_valid else
        "\033[91m" + 'Inválido' + "\033[0m" + "\033[93m" +
        "\nFormato permitido: (xx) 9xxxx-xxxx ou (xx) 9xxxxxxxx ou xx 9xxxxxxxx" + "\033[0m"}")