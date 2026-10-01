from package.objetos import *
objetos = []

objeto_cadastrado = cadastrar_objeto(objetos)
print(objeto_cadastrado)

resultado = localizar_por_codigo(objetos, 1)
print('O resultado da busca: ')
print(resultado)