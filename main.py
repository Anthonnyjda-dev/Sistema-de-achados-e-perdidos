from package.objetos import (
    cadastrar_objeto,
    listar_objetos,
    atualizar_objeto,
    remover_objeto
)
from package.buscas import (
    buscar_por_codigo,
    buscar_por_nome,
    buscar_por_categoria,
    buscar_por_local,
    buscar_por_tipo,
    buscar_por_status
)
from package.devolucoes import registrar_devolucao
from package.relatorios import (
    ordenar_objetos,
    mostrar_estatisticas,
    mostrar_por_categoria,
    mostrar_devolucoes
)
from package.validacoes import ler_inteiro


def exibir_menu():
    print('\n===== ACHADOS E PERDIDOS =====')
    print('1  - Cadastrar objeto')
    print('2  - Listar objetos')
    print('3  - Buscar objetos')
    print('4  - Atualizar objeto')
    print('5  - Remover objeto')
    print('6  - Registrar devolução')
    print('7  - Listar devoluções')
    print('8  - Ordenar objetos')
    print('9  - Estatísticas')
    print('10 - Objetos por categoria')
    print('0  - Sair')


def mostrar_resultados(resultados):
    if resultados == []:
        print('Nenhum objeto encontrado.')
    else:
        listar_objetos(resultados)


def menu_busca(objetos):
    print('\n--- BUSCAR POR ---')
    print('1 - Código')
    print('2 - Nome')
    print('3 - Categoria')
    print('4 - Local')
    print('5 - Tipo (perdido/encontrado)')
    print('6 - Status')

    try:
        opcao = int(input('Escolha o tipo de busca: '))
    except ValueError:
        print('Digite apenas números.')
        return

    match opcao:
        case 1:
            codigo = ler_inteiro('Informe o código: ')
            objeto = buscar_por_codigo(objetos, codigo)
            if objeto is None:
                print('Nenhum objeto encontrado.')
            else:
                listar_objetos([objeto])
        case 2:
            nome = input('Digite o nome: ')
            mostrar_resultados(buscar_por_nome(objetos, nome))
        case 3:
            categoria = input('Digite a categoria: ')
            mostrar_resultados(buscar_por_categoria(objetos, categoria))
        case 4:
            local = input('Digite o local: ')
            mostrar_resultados(buscar_por_local(objetos, local))
        case 5:
            tipo = input('Digite o tipo: ')
            mostrar_resultados(buscar_por_tipo(objetos, tipo))
        case 6:
            status = input('Digite o status: ')
            mostrar_resultados(buscar_por_status(objetos, status))
        case _:
            print('Opção de busca inexistente.')


def escolher_campo():
    print('\n--- ORDENAR POR ---')
    print('1 - Nome')
    print('2 - Data')
    print('3 - Categoria')
    print('4 - Local')
    print('5 - Status')

    try:
        opcao = int(input('Escolha o campo: '))
    except ValueError:
        print('Digite apenas números.')
        return None

    match opcao:
        case 1:
            return 'nome'
        case 2:
            return 'data'
        case 3:
            return 'categoria'
        case 4:
            return 'local'
        case 5:
            return 'status'
        case _:
            print('Campo inexistente.')
            return None


def main():
    objetos = []
    devolucoes = []
    codigos_utilizados = []

    while True:
        exibir_menu()

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Digite apenas números.')
            continue

        match opcao:
            case 1:
                novo = cadastrar_objeto(objetos, codigos_utilizados)
                if novo is not None:
                    print('Objeto cadastrado! Código:', novo['codigo'])
            case 2:
                listar_objetos(objetos)
            case 3:
                menu_busca(objetos)
            case 4:
                codigo = ler_inteiro('Informe o código que será atualizado: ')
                atualizar_objeto(objetos, codigo)
            case 5:
                codigo = ler_inteiro('Informe o código que será removido: ')
                remover_objeto(objetos, codigo)
            case 6:
                codigo = ler_inteiro('Informe o código do objeto devolvido: ')
                registrar_devolucao(objetos, devolucoes, codigo)
            case 7:
                mostrar_devolucoes(devolucoes)
            case 8:
                campo = escolher_campo()
                if campo is not None:
                    ordenados = ordenar_objetos(objetos, campo)
                    listar_objetos(ordenados)
            case 9:
                mostrar_estatisticas(objetos)
            case 10:
                mostrar_por_categoria(objetos)
            case 0:
                print('Sistema encerrado.')
                break
            case _:
                print('Opção inexistente.')


if __name__ == '__main__':
    main()
