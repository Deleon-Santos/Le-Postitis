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
    [sg.Text('Gerenciador de Tarefas',font=("Any",20,"bold"))],
    [sg.Text("Titulo",font=("Any",9,))],
    [sg.Input('Título da Tarefa',key="-TITULO-")],
    [sg.Text("Descrição",font=("Any",9,))],
    [sg.Multiline('Descrição da Tarefa',key="-DESC-",size=(43,5))],
    [sg.Text("Data",font=("Any",9,))],
    [sg.Input('Data Limite (AAAA-MM-DD)',key="-DATA-")],
    [sg.Text("Prioridade",font=("Any",9,))],
    [sg.Radio('Alta','RADIO', key='-BAIXA-'),sg.Radio('Média', 'RADIO',key='-MEDIA-'),sg.Radio('Baixa', 'RADIO',default=True, key='-ALTA-')],
    
    
    [sg.Button('Adicionar Tarefa')],
    
    [sg.Button('Sair')],
    [sg.Text('Tarefas Ativas:'),sg.T("",key="-SN-")],]
   
col2= [[sg.P(), sg.Multiline( key='tarefas',size=(40,23)),sg.P() ],
       [sg.Push(),sg.B("Anterior"),sg.B('Proxima'),sg.Push()]]

layout=[
    [sg.TabGroup([
       [sg.Tab("TEREFAS",col)],
       [sg.Tab("POSTITS",col2)]
        ])]
]

window = sg.Window('Gerenciador de Tarefas', layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    elif event == 'Adicionar Tarefa':
        titulo = values['-TITULO-']
        if not titulo:
            sg.popup("Adicione um titulo")
        
        descricao = values['-DESC-']
        if not descricao:
            sg.popup("Adicione uma descrição")
        data_limite = values['-DATA-']
        if not data_limite:
            sg.popup("Adicione uma data")

        if values['-ALTA-']== True:
            prioridade =  "Alto"
        elif values['-BAIXA-']== True:
            prioridade = "Baixo"
        else:
            prioridade = "Media"

        tarefa = {
            "titulo": titulo,
            "descricao": descricao,
            "data_limite": data_limite,
            "prioridade": prioridade
        }
        window['-SN-'].update("Tarefa Agendada")

window.close()