"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_oculta = 'Abominavel'.lower()

palavra_adivinha = '*' * len(palavra_oculta)

print(f'Descubra a palavra em {palavra_adivinha}')

tentativa = 0

while tentativa < 5:

    letra = input('Escolha um letra: ').lower()

    if len(letra) == 1 and letra.isalpha:
    
        if letra in palavra_oculta:
            
            nova_palavra_adivinha = ''
            
            for i in range(len(palavra_oculta)):
                
                if letra == palavra_oculta[i]:
                   
                    nova_palavra_adivinha += letra
                  
                else:
                    nova_palavra_adivinha += palavra_adivinha[i]
            palavra_adivinha = nova_palavra_adivinha
           
            print(palavra_adivinha)

        else:  
            print('Letra não encontrada na palavra oculta')
            tentativa += 1

    else:
        print('Inválido perdeu uma chance')
        tentativa += 1

    if '*' not in palavra_adivinha:
        print(f"Você adivinhou a palavra: {palavra_adivinha}")
        break

if "*" in palavra_adivinha:
    print(f'Suas tentativas acabaram a palavra oculta era {palavra_oculta}')
    