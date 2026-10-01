from package.objetos import (
    atualizar_objeto,
    cadastrar_objeto,
    listar_objetos,
    localizar_por_codigo,
    remover_objeto,
)


def executar_testes_manuais():
    """Menu temporário para testar as funções do módulo objetos."""
    objetos = []

    while True:
        print('\n--- TESTES DO MÓDULO OBJETOS ---')
        print('1 - Cadastrar objeto')
        print('2 - Listar objetos')
        print('3 - Localizar objeto por código')
        print('4 - Atualizar objeto')
        print('5 - Remover objeto')
        print('0 - Encerrar testes')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            objeto_cadastrado = cadastrar_objeto(objetos)
            print('Retorno do cadastro:', objeto_cadastrado)

        elif opcao == '2':
            listar_objetos(objetos)

        elif opcao == '3':
            codigo = int(input('Informe o código procurado: '))
            resultado = localizar_por_codigo(objetos, codigo)
            print('Resultado da busca:', resultado)

        elif opcao == '4':
            codigo = int(input('Informe o código que será atualizado: '))
            atualizar_objeto(objetos, codigo)

        elif opcao == '5':
            codigo = int(input('Informe o código que será removido: '))
            remover_objeto(objetos, codigo)

        elif opcao == '0':
            print('Testes encerrados.')
            break

        else:
            print('Opção inválida.')


if __name__ == '__main__':
    executar_testes_manuais()
    
