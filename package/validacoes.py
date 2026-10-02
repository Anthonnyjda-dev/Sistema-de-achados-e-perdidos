def ler_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto != "":
            return texto
        print("O campo não pode ficar vazio.")

def validar_data():
    while True:
        dia = ler_inteiro("Digite o dia: ")
        mes = ler_inteiro("Digite o mês: ")
        ano = ler_inteiro("Digite o ano: ")

        if mes < 1 or mes > 12:
            print("mês inválido")
            continue

        if ano < 1:
            print("Ano inválido. ")
            continue

        meses_30_dias = (4,6,9,11)

        if mes == 2:
            ano_bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
            ultimo_dia = 29 if ano_bissexto else 28

            if dia < 1 or dia > ultimo_dia:
                print("Dia inválido para fevereiro.")
                continue

        elif mes in meses_30_dias:
            if dia < 1 or dia > 30:
                print("Dia inválido para esse mês.")
                continue
        else:
            if dia < 1 or dia > 31:
                print("Dia inválido.")
                continue

        return (dia,mes,ano)
