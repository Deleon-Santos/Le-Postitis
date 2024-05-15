import PySimpleGUI as sg

# Lista para armazenar tarefas como post-its
tarefas_postits = []
id_count = 0

# Definir função para atualizar lista de tarefas
def atualizar_tarefas():
    global id_count
    id_count += 1
    tarefa = {
        "id": id_count,
        "titulo": values['-TITULO-'],
        "descricao": values['-DESC-'],
        "data_limite": values['-DATA-'],
        "prioridade": values['-PRIORIDADE-'],
        "concluida": values['-SN-'],
        "cor_prioridade": "red" if values['-PRIORIDADE-'] == "Alta" else 
                          "yellow" if values['-PRIORIDADE-'] == "Média" else "green"
    }
    tarefas_postits.append(tarefa)
    sg.popup("Tarefa Agendada")

# Criar interface gráfica
col = [
    [sg.Text('Gerenciador de Tarefas', font=("Any", 20, "bold"))],
    [sg.Text("Título")], [sg.Input('Título da Tarefa', key="-TITULO-")],
    [sg.Text("Descrição")], [sg.Multiline('Descrição da Tarefa', key="-DESC-", size=(43, 5))],
    [sg.Text("Data Limite")], [sg.Input('Data Limite (AAAA-MM-DD)', key="-DATA-")],
    [sg.Text("Prioridade")],
    [sg.Radio('Alta', 'PRIORIDADE', key='-PRIORIDADE-', default=True), 
     sg.Radio('Média', 'PRIORIDADE', key='-PRIORIDADE-'), 
     sg.Radio('Baixa', 'PRIORIDADE', key='-PRIORIDADE-')],
    [sg.Text("ID Atividade")], [sg.Input('', key="-ID-", size=(5,1)),sg.Checkbox("Concluída", key="-SN-")],
    [sg.Button('Adicionar Tarefa'),sg.Button('atualiza Tarefa'),sg.Button('excluir Tarefa')],
    [sg.Button('Pesquisar'),sg.Button('Sair')],
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
            task_list_content = ''
            for tarefa in tarefas_postits:
                concluida = "Sim" if tarefa["concluida"] else "Não"
                task_list_content += f"ID: {tarefa['id']}\nTítulo: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\nData Limite: {tarefa['data_limite']}\nConcluída: {concluida}\nPrioridade: {tarefa['prioridade']}\n\n"
            window['tarefas'].update(task_list_content)

window.close()

