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

print("\n--- TESTE: MAIÚSCULAS E MINÚSCULAS ---")
print(buscar_por_nome(objetos, "CARTEIRA"))

print("\n--- TESTE: BUSCA PARCIAL ---")
print(buscar_por_nome(objetos, "CART"))
