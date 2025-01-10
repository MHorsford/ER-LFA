class CPFValidator:
    @staticmethod
    def validate(cpf: str) -> bool:
        # Verifica se o comprimento é exatamente 14 caracteres
        if len(cpf) != 14:
            print("\033[93m" + "A sentença não possui o comprimento igual a 14 (XXX.XXX.XXX-XX)!" + "\033[0m")
            return False

        # Verifica se o formato do CPF é válido
        if not (cpf[:3].isdigit() and cpf[3] == '.' and
                cpf[4:7].isdigit() and cpf[7] == '.' and
                cpf[8:11].isdigit() and cpf[11] == '-' and
                cpf[12:].isdigit()):
            print("\033[93m" + "O formato da sentença não corresponde a 'xxx.xxx.xxx-xx' onde x pertence a N!" + "\033[0m")
            return False

        return True


if __name__ == "__main__":

    cpfs = [
        "123.456.789-09",  # Aceito
        "000.000.000-00",  # Aceito
        "123.456.789-0",   # Rejeitado (faltando um dígito no final)
        "111.111.11-11",   # Rejeitado (faltando um bloco de dígitos)
        "abc.def.ghi-jk",  # Rejeitado (não contém apenas números)
        "12345678909",     # Rejeitado (faltam os separadores)
    ]

    for cpf in cpfs:
        print(f"'{cpf}': {"\033[92m" + 'Válido' + "\033[0m" if CPFValidator.validate(cpf) else 
        "\033[91m" + 'Inválido' + "\033[0m"}")
