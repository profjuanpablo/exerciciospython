alunos = []
testes = []
provas =[]
trabalhos = []
medias=[]

print(f"tamanho inicial array {len(alunos)}")
print("--------------------")
i = 0
while len(alunos)!=3:
    a = input("Digite  o nome: ")
    alunos.append(a)

    tes = float(input("Digite nota teste: "))
    testes.append(tes)

    prov = float(input("Digite nota prova: "))
    provas.append(prov)

    trab = float(input("Digite nota trabalho: "))
    trabalhos.append(trab)

    medias.append( ( (testes[i]+provas[i]+trabalhos[i]) /3)  )
    i = i+1

for media in medias:
    print(f" média: {media} ")

