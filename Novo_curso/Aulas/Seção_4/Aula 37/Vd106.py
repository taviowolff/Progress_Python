"""
Argumento posicional x Argumento não posicional ou nomeado
"""

def soma (x,y,z):
    print(f'{x=} y={y} {z=}','|','x+y+z=', x+y+z)

soma(1,2,3)
soma(x=1,z=2,y=3)