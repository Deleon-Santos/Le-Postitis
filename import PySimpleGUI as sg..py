import PySimpleGUI as sg

# Lista para armazenar tarefas como post-its
tarefas_postits = []
id_count = 0

# Definir função para atualizar lista de tarefas
def atualizar_tarefas():
    global id_count
    id_count += 1
    tarefa = {
        "Id": id_count,
        "Titulo": values['-TITULO-'],
        "Descricao": values['-DESC-'],
        "Prazo": values['-DATA-'],
        "Prioridade": prioridade,
        "Concluida": values['-SN-'],}
        
    tarefas_postits.append(tarefa)
    for tarefa in tarefas_postits:
        for k , v in tarefa.items():

            window['tarefas'].print({k,v})

    sg.popup("Tarefa Agendada")

# Criar interface gráfica
col = [
    [sg.Text('GERENCIADOR DE TAREFAS', font=("Any", 20, "bold"))],
    [sg.Text("Título")], [sg.Input('Título da Tarefa', key="-TITULO-")],
    [sg.Text("Descrição")], [sg.Multiline('Descrição da Tarefa', key="-DESC-", size=(43, 5))],
    [sg.Text("Data Limite")], [sg.Input('Data Limite (AAAA-MM-DD)', key="-DATA-")],
    [sg.Text("Prioridade")],
    [sg.Radio('Alta', 'PRIORIDADE', key='-ALTA-', default=True), 
     sg.Radio('Média', 'PRIORIDADE', key='-MEDIA-'), 
     sg.Radio('Baixa', 'PRIORIDADE', key='-BAIXA-')],
    [sg.Text("ID Atividade")], [sg.Input('', key="-ID-", size=(5,1)),sg.Checkbox("Concluída", key="-SN-")],
    [sg.Button('Adicionar Tarefa'), sg.Button('Atualizar Tarefa'), sg.Button('Excluir Tarefa')],
    [sg.Text("Pesquisar por ID")], [sg.Input('', key="-SEARCH_ID-", size=(5,1)), sg.Button('Pesquisar')],
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
            if values['-ALTA-'] ==True:
                prioridade = 'Alta'
            elif values['-MEDIA-']  ==True:
                prioridade = 'Média'
            else: 
                prioridade = 'Baixa' 
            atualizar_tarefas()
            # Atualizar a lista de tarefas no segundo tab (POSTITS)
            task_list_content = ''
            for tarefa in tarefas_postits:
                
                
                concluida = "Sim" if tarefa["concluida"] else "Não"
                task_list_content += f"ID: {tarefa['id']}\nTítulo: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\nData Limite: {tarefa['data_limite']}\nConcluída: {concluida}\nPrioridade: {prioridade}\n\n"
            
            print(tarefas_postits)

    elif event == 'Pesquisar':
        search_id = int(values['-SEARCH_ID-']) if values['-SEARCH_ID-'].isdigit() else None
        if search_id is None:
            sg.popup("Digite um ID válido para pesquisar!")
        else:
            found_task = next((tarefa for tarefa in tarefas_postits if tarefa['id'] == search_id), None)
            if found_task:
                window['-ID-'].update(found_task['id'])
                window['-TITULO-'].update(found_task['titulo'])
                window['-DESC-'].update(found_task['descricao'])
                window['-DATA-'].update(found_task['data_limite'])
                window['-PRIORIDADE-'].update(True if found_task['prioridade'] == 'Alta' else False)
                window['-SN-'].update(found_task['concluida'])
            else:
                sg.popup(f"Tarefa com ID {search_id} não encontrada!")

window.close()


'''"cor_prioridade": "red" if values['-PRIORIDADE-'] == "Alta" else 
                          "yellow" if values['-PRIORIDADE-'] == "Média" else "green"'''
    