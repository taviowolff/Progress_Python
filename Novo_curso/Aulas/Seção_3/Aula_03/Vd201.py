class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        raise NotImplementedError

    def dormir(self):
        print(f'{self.nome} está dormindo.')

    
class Gato(Animal):
    def fazer_som(self):
        print(f'{self.nome} está miando.')

class Cachorro(Animal):
    def fazer_som(self):
        print(f'{self.nome} está latindo.')


cachorro = Cachorro('Dino')
print(cachorro.nome)
cachorro.fazer_som()

gato = Gato('Aiba')
print(gato.nome)
cachorro.dormir()
