import name_validator
import cpf_validator
import email_validator
import password_validator
import phone_validator


def menu():
    psw = password_validator.PasswordValidator()

    while True:
        print("Menu:")
        print("1 - Validar Nome\n2 - Validar CPF\n3 - Validar E-mail\n"
              "4 - Validar Senha\n5 - Validar Telefone\n0 - Sair")


        option = int(input("Escolha uma opção: "))
        if option == 1:
            name = input("Digite o nome: ")
            if name_validator.NameValidator.validate_name(name):
                print("\033[92m" + "Nome válido" + "\033[0m")
            else:
                print("\033[91m" + "Nome inválido" + "\033[0m")
        elif option == 2:
            cpf = input("Digite o CPF: ")
            if cpf_validator.CPFValidator.validate(cpf):
                print("\033[92m" + "CPF válido" + "\033[0m")
            else:
                print("\033[91m" + "CPF inválido" + "\033[0m")
        elif option == 3:
            email = input("Digite o e-mail: ")
            if email_validator.EmailValidator.validator_email(email):
                print("\033[92m" + "E-mail válido" + "\033[0m")
            else:
                print("\033[91m" + "E-mail inválido" + "\033[0m")
        elif option == 4:
            password = input("Digite a senha: ")
            if psw.validate_password(password):
                print("\033[92m" + "Senha valida" + "\033[0m")
            else:
                print("\033[91m" + "Senha inválida" + "\033[0m")
        elif option == 5:
            phone = input("Digite o telefone: ")
            if phone_validator.PhoneNumberValidator.is_valid_phone_number(phone):
                print("\033[92m" + "Telefone válido" + "\033[0m")
            else:
                print("\033[93m" + "Formato permitido: (xx) 9xxxx-xxxx ou (xx) 9xxxxxxxx ou xx 9xxxxxxxx" + "\033[0m")
                print("\033[91m" + "Telefone inválido" + "\033[0m")
        elif option == 0:
            break

menu()
