'''
Manipulando strings - aula 16
* String indices
* Fatiamento de strings [inicio:fim:passo]
Essas funções podem ser usadas diretamente em cada tipo

Voce pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
'''

# positivos   [012345678]
texto       = 'Python_s2'
# negativos  -[987654321]

nova_str = texto[-9]
print(nova_str)

nova_str1 = texto[-9:-3]
print(nova_str1)

nova_str2 = texto[0]
print(nova_str2)

nova_str3 = texto[0:9]
print(nova_str3)

nova_str4 = texto[0:8:2] # começando do 0 e indo até 8 pulando de 2 em 2
print(nova_str4)

for letra in texto:
    print(letra)
