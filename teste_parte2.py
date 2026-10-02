from package.objetos import cadastrar_objeto
from package.buscas import (
    buscar_por_codigo,
    buscar_por_nome,
    buscar_por_categoria,
    buscar_por_local,
    buscar_por_tipo,
    buscar_por_status
)
from package.devolucoes import registrar_devolucao


objetos = []
devolucoes = []


print("\n--- CADASTRO ---")
cadastrar_objeto(objetos)


print("\n--- TESTE: BUSCA POR CÓDIGO ---")
print(buscar_por_codigo(objetos, 1))


print("\n--- TESTE: BUSCA POR NOME ---")
nome = input("Digite um nome para buscar: ")
print(buscar_por_nome(objetos, nome))


print("\n--- TESTE: BUSCA POR CATEGORIA ---")
categoria = input("Digite uma categoria para buscar: ")
print(buscar_por_categoria(objetos, categoria))


print("\n--- TESTE: BUSCA POR LOCAL ---")
local = input("Digite um local para buscar: ")
print(buscar_por_local(objetos, local))


print("\n--- TESTE: BUSCA POR TIPO ---")
tipo = input("Digite o tipo para buscar: ")
print(buscar_por_tipo(objetos, tipo))


print("\n--- TESTE: BUSCA POR STATUS ---")
status = input("Digite o status para buscar: ")
print(buscar_por_status(objetos, status))


print("\n--- TESTE: CÓDIGO INEXISTENTE ---")
print(buscar_por_codigo(objetos, 999))


print("\n--- TESTE: DEVOLUÇÃO ---")
registrar_devolucao(objetos, devolucoes, 1)


print("\n--- TESTE: DEVOLVER NOVAMENTE ---")
registrar_devolucao(objetos, devolucoes, 1)


print("\n--- TESTE: DEVOLVER OBJETO INEXISTENTE ---")
registrar_devolucao(objetos, devolucoes, 999)


print("\n--- OBJETOS ---")
print(objetos)


print("\n--- DEVOLUÇÕES ---")
print(devolucoes)