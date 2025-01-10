class PasswordValidator:
    def __init__(self):
        # Definição dos alfabetos
        self.alphabet_sigma = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.alphabet_gamma = set("!@#$%&*()-_")
        self.alphabet_n = set("0123456789")

    def validate_password(self, password: str) -> bool:
        # Verifica se a senha tem exatamente 8 caracteres
        if len(password) != 8:
            print("\033[93m" + "A senha deve ter exatamente 8 caracteres." + "\033[0m")
            return False

        # Verifica se contém pelo menos uma letra (Σ)
        if not any(char in self.alphabet_sigma for char in password):
            print("\033[93m" + "A senha deve conter pelo menos uma letra (Σ)." + "\033[0m")
            return False

        # Verifica se contém pelo menos um número (N)
        if not any(char in self.alphabet_n for char in password):
            print("\033[93m" + "A senha deve conter pelo menos um número (N)." + "\033[0m")
            return False

        # Verifica se todos os caracteres pertencem aos alfabetos permitidos
        if not all(char in self.alphabet_sigma or char in self.alphabet_gamma or char in self.alphabet_n for char in password):
            print("\033[93m" + "A senha contém caracteres inválidos." + "\033[0m")
            return False

        return True


if __name__ == "__main__":
    validator = PasswordValidator()

    passwords = [
        "518R2r5e",  # Aceito
        "F123456A",  # Aceito
        "1234567T",  # Aceito
        "ropsSoq0",  # Aceito
        "abcd!123",  # Aceito
        "abcd123",   # Rejeitado (não tem exatamente 8 caracteres)
        "abcdefgH",  # Rejeitado (não contém N)
        "12345678",  # Rejeitado (não contém Σ)
        "ABCD!@#$",  # Rejeitado (não contém N)
    ]

    for password in passwords:
        is_valid = validator.validate_password(password)
        print(f"'{password}': {'\033[92mVálido\033[0m' if is_valid else '\033[91mInválido\033[0m'}")
