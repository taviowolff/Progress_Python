# Módulos padrão do Python (import, fromm as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namescape do módulo
# Desvatagens: nomes grandes

# import sys

# platform = 'A minha plataforma'
# print(sys.platform, 'Planataforma do sys')
# print(platform)


# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform

# print(platform)

# platform = 'A minha' # subreescrenveu a função do módulo com a variável 

# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

# alias 2 - from nome_modulo import objeto as apelido
# from sys import platform as pf, exit as ex

# print(pf)

# Vantagens: você pode reversar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem


# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import *
import os
from time import sleep


print(platform)
sleep(2)
os.system('cls')

exit()