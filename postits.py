import sys
import datetime
import PySimpleGUI as sg
# Importar bibliotecas
import sys
import datetime
import PySimpleGUI as sg


# Definir funções
def criar_postit(tarefa, prioridade):
    if prioridade == "Alta":
        cor = "red"
    elif prioridade == "Média":
        cor = "yellow"
    else:
        cor = "green"

    layout = [
        [sg.Text(tarefa["titulo"], background_color=cor)],
        [sg.Text(tarefa["descricao"])],
        [sg.Text(f"Data Limite: {tarefa['data_limite']}")],
    ]

    window = sg.Window(tarefa["titulo"], layout)
    event, values = window.read()
    window.close()


def atualizar_tarefas():
    pass  # Implementar a atualização da lista de tarefas e dos postits


def agendar_tarefas():
    pass  # Implementar a verificação de tarefas vencidas



    # Criar interface gráfica
col = [
    [sg.Text('Gerenciador de Tarefas')],
    [sg.Input('Título da Tarefa')],
    [sg.Multiline('Descrição da Tarefa',key="-IMPUT-")],
    [sg.Input('Data Limite (AAAA-MM-DD)')],
    [sg.Radio('Alta', 'Prioridade', key='prioridade1')],
    [sg.Radio('Média', 'Prioridade', key='prioridade2')],
    [sg.Radio('Baixa', 'Prioridade', key='prioridade3')],
    [sg.Button('Adicionar Tarefa')],
    [sg.Button('Salvar Alterações')],
    [sg.Button('Sair')],
    [sg.Text('Tarefas Ativas:')],]
   
col2= [[sg.Multiline( key='tarefas') , sg.VerticalSeparator()],]
layout=[
   [ sg.Column(col),sg.Column(col2)],
]

window = sg.Window('Gerenciador de Tarefas', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    elif event == 'Adicionar Tarefa':
        titulo = values['Título da Tarefa']
        descricao = values['Descrição da Tarefa']
        data_limite = values['Data Limite']
        prioridade = values.get('Prioridade', 'Baixa')

        tarefa = {
            "titulo": titulo,
            "descricao": descricao,
            "data_limite": datetime.datetime.strptime(data_limite, "%Y-%m-%d").date(),
            "prioridade": prioridade,
        }


window.close()