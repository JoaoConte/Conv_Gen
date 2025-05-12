z = '9.9.9.99.99.999' 
a = '9.9.9.999.9999'  
conta2 = '9999999999'

import re

def aplicar_mascara(campo, mascara):
    campo_limpo = re.sub(r'\W+', '', campo)
    resultado = []
    j = 0
    
    for i in range(len(mascara)):
        if j >= len(campo_limpo):
            break
        
        if mascara[i] == '#':
            resultado.append(campo_limpo[j])
            j += 1
        else:
            resultado.append(mascara[i])
    
    return ''.join(resultado)

# Exemplo de uso
campo = "1.1.01.0011"
mascara = "#.#.##.####"
campo_mascarado = aplicar_mascara(campo, mascara)
print(campo_mascarado)  # Saída: 123-abc-456













# #lista = []
# #cont = sum([1 for i in a if i == '.'])
# # contador = 1
# # while contador <= cont:
# #     if len(lista) == 0:
# #         pos1 = a.find('.')
# #         lista.append(pos1)
# #         pos2 = pos1
# #         contador = contador + 1
# #     else:
# #         pos1 = a.find('.', pos2+1)
# #         lista.append(pos1)
# #         pos2 = pos1
# #         contador = contador + 1

# conta = a.replace('9','{}')
# print(conta)
# conta1 = conta2.format(*conta)

#     # if len(conta) == 1:
#     #     novaconta = conta
#     # if len(conta) > 1 and posic_masc == 1:
#     #     novaconta = conta[0]+'.'+
# print(conta1)







# b= a.find('.')
# print(b, ' - ', len(str(b)))
# c = a.find('.', b+1)
# print(c, ' - ', len(str(c)))
# d = a.find('.', c+1)
# print(d, ' - ', len(str(d)))
# e = a.find('.', d+1)
# print(e, ' - ', len(str(e)))
# f = a.find('.', e+1)
# print(f)
