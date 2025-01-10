class EmailValidator:

    @staticmethod
    def validator_email(email: str) -> bool:
        # Verifica se a sentença contém um, e apenas um, símbolo "@"
        if email.count('@') != 1:
            print("\033[93m" + "A sentença deve conter um, e apenas um, símbolo '@'" + "\033[0m")
            return False

        username, domain = email.split('@')

        # Verifica se a sentença não começa com o símbolo "@"
        if username == '':
            print("\033[93m" + "A sentença não deve começar com o símbolo '@'" + "\033[0m")
            return False


        # O username deve conter pelo menos um caractere alfanumérico
        if not any(char.isalnum() for char in username):
            print("\033[93m" + "O username deve conter pelo menos um caractere alfanumérico." + "\033[0m")
            return False

        # Verifica se a sentença termina com ".com.br" ou ".br"
        if not (domain.endswith(".com.br") or domain.endswith(".com") or domain.endswith(".br")):
            print("\033[93m" + "A sentença deve terminar com '.com.br' ou '.br'" + "\033[0m")
            return False

        # Verifica se há pelo menos uma letra entre o "@" e a terminação
        domain_parts = domain.split('.')
        if len(domain_parts) > 1 and not any(char.isalpha() for char in domain_parts[0]):
            print("\033[93m" + "Deve haver, pelo menos, uma letra entre o '@' e a terminação" + "\033[0m")
            return False

        # Verifica se não há letras maiúsculas após o "@" até a terminação
        if any(char.isupper() for char in domain_parts[0]):
            print("\033[93m" + "Não podem haver letras maiúsculas após o '@'" + "\033[0m")
            return False

        # Verifica se não há símbolos inválidos entre o "@" e a terminação
        valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789-")
        if not all(char in valid_chars for char in domain_parts[0]):
            print("\033[93m" + "A sentença deve conter apenas caracteres válidos após o '@'" + "\033[0m")
            return False

        return True


if __name__ == "__main__":

    emails = [
        "a@a.br",  # Aceito
        "divulga@ufpa.br",  # Aceito
        "usuario123@dominio.com.br",  # Aceito
        "user@dominio123.com.br",  # Aceito
        "T@teste.br",  # Aceito
        "@",  # Rejeitado (somente o símbolo "@")
        "a@.br",  # Rejeitado (sem caracteres entre o "@" e a terminação)
        "user@domínio.com.br",  # Rejeitado (contém caractere inválido 'í')
        "---@gmail.com"
    ]

    for email in emails:
        is_valid = EmailValidator.validator_email(email)
        print(f"'{email}': {"\033[92m" + 'Válido' + "\033[0m" if is_valid else
        "\033[91m" + 'Inválido' + "\033[0m"}")
