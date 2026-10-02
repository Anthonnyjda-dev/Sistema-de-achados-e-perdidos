from package.relatorios import (
    ordenar_objetos,
    mostrar_estatisticas,
    mostrar_por_categoria,
    mostrar_devolucoes
)
from package.devolucoes import registrar_devolucao


objetos = [
    {'codigo': 1, 'nome': 'Carteira', 'categoria': 'Documento', 'descricao': 'Preta',
     'local': 'Biblioteca', 'data': (10, 3, 2026), 'tipo': 'perdido',
     'status': 'Procurando', 'responsavel': 'Maria'},
    {'codigo': 2, 'nome': 'mochila', 'categoria': 'Material', 'descricao': 'Azul',
     'local': 'Pátio', 'data': (5, 1, 2026), 'tipo': 'encontrado',
     'status': 'Disponível', 'responsavel': 'Joao'},
    {'codigo': 3, 'nome': 'Anel', 'categoria': 'documento', 'descricao': 'Dourado',
     'local': 'Sala 2', 'data': (20, 2, 2025), 'tipo': 'encontrado',
     'status': 'Disponível', 'responsavel': 'Ana'},
]
devolucoes = []


def mostrar_codigos(lista):
    """Mostra só os códigos, para conferir a ordem rapidamente."""
    codigos = []
    for objeto in lista:
        codigos.append(objeto['codigo'])
    print(codigos)


print('\n--- TESTE: ORDENAR LISTA VAZIA ---')
print(ordenar_objetos([], 'nome'))          # esperado: []

print('\n--- TESTE: CAMPO INVÁLIDO ---')
print(ordenar_objetos(objetos, 'cor'))      # esperado: aviso e []

print('\n--- TESTE: ORDENAR POR NOME (esperado [3, 1, 2]) ---')
mostrar_codigos(ordenar_objetos(objetos, 'nome'))

print('\n--- TESTE: ORDENAR POR DATA (esperado [3, 2, 1]) ---')
mostrar_codigos(ordenar_objetos(objetos, 'data'))

print('\n--- TESTE: ORDENAR POR CATEGORIA (esperado [1, 3, 2], empate mantém a ordem) ---')
mostrar_codigos(ordenar_objetos(objetos, 'categoria'))

print('\n--- TESTE: LISTA ORIGINAL NÃO MUDOU (esperado [1, 2, 3]) ---')
mostrar_codigos(objetos)

print('\n--- TESTE: ESTATÍSTICAS ANTES DA DEVOLUÇÃO ---')
mostrar_estatisticas(objetos)

print('\n--- TESTE: OBJETOS POR CATEGORIA (esperado documento: 2, material: 1) ---')
mostrar_por_categoria(objetos)

print('\n--- TESTE: DEVOLUÇÃO DO OBJETO 1 (digite nome e data) ---')
registrar_devolucao(objetos, devolucoes, 1)

print('\n--- TESTE: ESTATÍSTICAS DEPOIS DA DEVOLUÇÃO ---')
mostrar_estatisticas(objetos)               # Procurando 0, Devolvidos 1

print('\n--- TESTE: LISTA DE DEVOLUÇÕES ---')
mostrar_devolucoes(devolucoes)