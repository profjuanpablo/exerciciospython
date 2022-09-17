"""
crie um algoritmo que receba um número À ser adivinhado
por um jogador
se ele acertar parabenizá-lo pelo acerto caso contrário
diga que ele errou.
"""
import random

num = random.randrange(1,10)
print(num)
resp= "s"
tentativas =1
while resp=="s":
    chute = int(input("DÊ o seu chute entre 1 e 10: "))
    if num==chute:
        print("ACertou")
        resp="n"
    else:
        print("Errou")
        tentativas= tentativas+1
        resp = str(input("Quer COntinuar? "))

    print(f"Você chutou {tentativas}x")

