alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 4.2},
    {"nome": "Carlos", "nota": 6.0},
    {"nome": "Diana", "nota": 9.8},
]

alunos_ordenado = sorted(alunos, key=lambda x: x["nota"], reverse=True)
print(f"Alunos ordenados: {alunos_ordenado}")

with open("notas.txt", "w") as arquivo:
    arquivo.writelines(f"aluno: {i["nome"]} tirou nota {i["nota"]}.\n" for i in alunos_ordenado)

alunos_aprovados = [aluno for aluno in alunos_ordenado if aluno["nota"] >= 6]
print(f"Alunos aprovados: {alunos_aprovados}")

alunos_reprovados = [aluno for aluno in alunos_ordenado if aluno["nota"] < 6]
print(f"Alunos reprovados: {alunos_reprovados}")


try:
    nova_nota = float(input("Digite a nota do novo aluno: "))
    novo_aluno = {"nome": "Eduardo", "nota": nova_nota}
    alunos.append(novo_aluno)
    print(f"Aluno {novo_aluno['nome']} adicionado com nota {novo_aluno['nota']}")
except ValueError:
    print("Nota inválida! Digite um número.")