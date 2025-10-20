#Biblioteca
import numpy as np

#Main
notas = []
nomes = []
# NOVA LISTA para armazenar os nomes dos alunos que ficam acima da média
nomes_acima_media =[]
NUMERO_ALUNOS = 5 #Definindo uma constante para ser mais legível

for i in range (NUMERO_ALUNOS):
    #Coleta do nome
    n= input("Por favor insira o nome do aluno %d: " % (i+1))
    nomes.append(n)

    #Coleta e Validação da Nota(Correção para aceitar vírgula)
    while True:
        try:
            #Pega a entrada,troca','por '.', e converte para float
            entrada = input("Por favor insira a nota do aluno %d: " % (i+1)).replace(',','.')
            j = float(entrada)
            if 0 <= j <= 10:
                notas.append(j)
                break
            else:
                print("Nota inválida.Por favor,digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida.Digite apenas números.")

# --- Processamento e Impressão de Resultados ---

# Média Geral da Turma (Usando NumPy)
media_geral = np.average(notas)
print("\n--- Resultados Iniciais ---")
print("A média da turma é %.2f" % media_geral)

#Aluno com maior nota
nosso_max = max(notas)

for i in range (NUMERO_ALUNOS):
    if(notas[i] == nosso_max):
        print("O aluno com maior nota é o %s (Nota: %.2f)" % (nomes[i],nosso_max))

    #--------------------------------------------------------
    #NOVO TRECHO: Média dos alunos acima da Média media_geral
    #(NOTA: Corrigi a indentação que estava no seu código original)
    #---------------------------------------------------------

soma_notas_acima_media = 0.0
contador_acima_media = 0

    #Percorrer a lista de Notas e Nomes (usamos range e índice 'i' para pegar o nome junto)
for i in range(NUMERO_ALUNOS):
    nota = notas[i]
    nome = nomes[i]

    if nota > media_geral:
            soma_notas_acima_media += nota
            contador_acima_media += 1
            nomes_acima_media.append(nome) #Armazena o nome!

    #Calcular a Média SÓ dos alunos que estão acima da Média Geral
media_acima_media = 0.0
if contador_acima_media > 0:
        media_acima_media = soma_notas_acima_media / contador_acima_media

    #Impressão do Resultado
print("\n--- Média de Notas Acima da Média Geral ---")
print(f"Total de alunos acima da média geral ({media_geral:.2f}: {contador_acima_media}")

    #Novo Print: Listando os nomes dos alunos acima da média:
if media_acima_media:
        print(f"Alunos que ficaram acima da média: {', '.join(nomes_acima_media)}")

if media_acima_media > 0:
        print("A Média dos melhores alunos(que ficaram acima da média geral) é: %.2f" % media_acima_media)
else:
        print("Não há alunos com nota superior à média geral para calcular essa média específica.")