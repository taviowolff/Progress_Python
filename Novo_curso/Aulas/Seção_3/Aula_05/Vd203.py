# Mantendo estados dentro da classe.

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando: 
            print(f'{self.nome} já está filmando.')
            return

        print(f'{self.nome} está filmando.')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando.')
            return
    
        print(f'{self.nome} está parando de filmar.')
        self.filmando = False

    def tirar_foto(self):
        if self.filmando:
            print(f'{self.nome} não tira foto filmando.')
            return

        print(f'{self.nome} tirou foto')

         
c1 = Camera('Canon')
c1.parar_filmar()
c1.filmar()
c1.tirar_foto()
c1.parar_filmar()
c1.tirar_foto()

c2 = Camera('Sony')
c2.tirar_foto()
c2.filmar()
c2.parar_filmar()
c2.parar_filmar()
