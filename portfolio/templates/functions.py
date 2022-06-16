import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def PontuacaoQuizz(quiz):

    pontuacao = 0

    if(quiz.questao_1 == "Apple"):
        pontuacao += 1

    if(quiz.questao_2 == 22):
        pontuacao += 1

    if(quiz.questao_3 == 2011):
        pontuacao += 1

    if(quiz.questao_4 == "Don't Repeat Yourself"):
        pontuacao += 1

    return pontuacao

def grafico_quiz_data(objects):
    data = {}
    for quizz in objects:
        data[quizz.nome] = PontuacaoQuizz(quizz)
        print(quizz.nome)

    return data

def grafico_quiz(objects):
    data = grafico_quiz_data(objects)
    users = list(data.keys())
    values = list(data.values())

    plt.bar(users,values,color = 'green', width = 0.3)

    plt.xlabel("Jogadores")
    plt.ylabel("Pontuação")
    plt.title("Quiz Programação Web")
    plt.savefig('portfolio/static/portfolio/images/grafico.png')


