class NameValidator:
    @staticmethod
    def validate_name(name: str) -> bool:
        # Divide o nome em partes
        parts = name.split()

        # Verifica se há exatamente duas partes (nome e sobrenome)
        if len(parts) != 2:
            return False

        for part in parts:
            # Verifica se a primeira letra é maiúscula
            if not ('A' <= part[0] <= 'Z'):
                return False

            # Verifica se as outras letras são minúsculas
            for char in part[1:]:
                if not ('a' <= char <= 'z'):
                    return False

        return True


if __name__ == "__main__":
    names = [
        "Alan Turing",  # Aceito
        "Noam Chomsky",  # Aceito
        "Ada Lovelace",  # Aceito
        "Marcos Horsford",  # Aceito
        "1Alan",  # Rejeitado
        "Alan",  # Rejeitado
        "A1an",  # Rejeitado
        "Alan turing",  # Rejeitado
        "Alan Turing123",  # Rejeitado
        "AlanTuring",  # Rejeitado
        "Marcos",  # Rejeitado
    ]

    for name in names:
        print(f"'{name}': {"\033[92m" + 'Válido' + "\033[0m" if NameValidator.validate_name(name) else
        "\033[91m" + 'Inválido' + "\033[0m"}")
