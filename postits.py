import PySimpleGUI as sg

# Lista para armazenar tarefas como post-its
tarefas_postits = []
current_task_index = 0

# Definir função para criar post-it
def criar_postit(tarefa):
    layout = [
        [sg.Text(tarefa["titulo"], background_color=tarefa["cor_prioridade"])],
        [sg.Text(tarefa["descricao"])],
        [sg.Text(f"Data Limite: {tarefa['data_limite']}")],
    ]
    window = sg.Window(tarefa["titulo"], layout)
    event, values = window.read()
    window.close()

# Definir função para atualizar lista de tarefas
def atualizar_tarefas():
    global tarefas_postits
    tarefas_postits.append({
        "titulo": values['-TITULO-'],
        "descricao": values['-DESC-'],
        "data_limite": values['-DATA-'],
        "prioridade": values['-PRIORIDADE-'],
        "cor_prioridade": "red" if values['-PRIORIDADE-'] == "Alta" else 
                           "yellow" if values['-PRIORIDADE-'] == "Média" else "green"
    })
    sg.popup("Tarefa Agendada")

# Criar interface gráfica
col = [
    [sg.Text('Gerenciador de Tarefas', font=("Any", 20, "bold"))],
    [sg.Text("Título"), sg.Input('Título da Tarefa', key="-TITULO-")],
    [sg.Text("Descrição"), sg.Multiline('Descrição da Tarefa', key="-DESC-", size=(43, 5))],
    [sg.Text("Data Limite"), sg.Input('Data Limite (AAAA-MM-DD)', key="-DATA-")],
    [sg.Text("Prioridade")],
    [sg.Radio('Alta', 'PRIORIDADE', key='-PRIORIDADE-', default=True), 
     sg.Radio('Média', 'PRIORIDADE', key='-PRIORIDADE-'), 
     sg.Radio('Baixa', 'PRIORIDADE', key='-PRIORIDADE-')],
    [sg.Button('Adicionar Tarefa')],
    [sg.Button('Sair')],
]

col2 = [
    [sg.Multiline('', key='tarefas', size=(40, 23))],
    [sg.Button('Anterior'), sg.Button('Próxima')],
]

layout = [
    [sg.TabGroup([
        [sg.Tab("TAREFAS", col)],
        [sg.Tab("POSTITS", col2)]
    ])]
]

window = sg.Window('Gerenciador de Tarefas', layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    elif event == 'Adicionar Tarefa':
        if not values['-TITULO-'] or not values['-DESC-'] or not values['-DATA-']:
            sg.popup("Preencha todos os campos!")
        else:
            atualizar_tarefas()
            # Atualizar a lista de tarefas no segundo tab (POSTITS)
            window['tarefas'].update('\n'.join([f"Título: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\nData Limite: {tarefa['data_limite']}\n" for tarefa in tarefas_postits]))

    elif event == 'Anterior':
        if current_task_index > 0:
            current_task_index -= 1
            criar_postit(tarefas_postits[current_task_index])

    elif event == 'Próxima':
        if current_task_index < len(tarefas_postits) - 1:
            current_task_index += 1
            criar_postit(tarefas_postits[current_task_index])

window.close()
