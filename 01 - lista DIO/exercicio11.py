nomeAluno = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if (media >= 7):
    situacao = "aprovado"
    mensagem = f"O aluno {nomeAluno} está {situacao}"
else:
    situacao = "reprovado"
    mensagem = f"O aluno {nomeAluno} está {situacao}"

print(mensagem)

