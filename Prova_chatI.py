n= int(input('Digite o numero de Alunos: '))
alunos= []

for nome in range (0,n):
    nome = input('Digite o nome do aluno: ')
    notas= 0
    for j in range(1,4):
        nota = float(input(f"Digite a nota {j} do aluno {nome}: "))
        notas += nota
    media= notas / j
    aprovado= "Aprovado" if media >= 7.0 else "Reprovado"
        
    alunos += [{
        "nome": nome,
        "notas": notas,
        "media": media,
        "aprovado": aprovado}]
    
soma_medias = 0
contador_medias = 0
print("\nResultados:")
for aluno in alunos:
    soma_medias += aluno["media"]
    contador_medias += 1
    print(f"Aluno: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['aprovado']}\n")
    
media_geral = soma_medias / contador_medias
print(f"Média geral da turma: {media_geral:.2f}")
    

    
