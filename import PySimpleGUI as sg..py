import PySimpleGUI as sg

# Lista para armazenar tarefas como post-its
tarefas_postits = []
id_contador = 0

# Definir função para atualizar lista de tarefas
def atualizar_tarefas(prioridade):
    global id_contador
    id_contador += 1
    tarefa = {
        "Id": id_contador,
        "Titulo": values['-TITULO-'],
        "Descricao": values['-DESC-'],
        "Prazo": values['-DATA-'],
        "Prioridade": prioridade,
        "Concluida": values['-SN-'],}
        
    tarefas_postits.append(tarefa)
           
    sg.popup("Tarefa Agendada")

def atualize():
        task_list_content = ''
        for tarefa in tarefas_postits:          
            concluida = "Sim" if tarefa["Concluida"] else "Não"
            task_list_content += f"ID: {tarefa['Id']}\nTítulo: {tarefa['Titulo']}\nDescrição: {tarefa['Descricao']}\nData Limite: {tarefa['Prazo']}\nConcluída: {concluida}\nPrioridade: {tarefa['Prioridade']}\n\n"
        
        window['tarefas'].update(task_list_content)
        print(tarefas_postits)


# Criar interface gráfica
col = [
    [sg.T("",size=(1,1),font=("Any",1))],
    [sg.Text('GERENCIADOR DE TAREFAS', font=("Any", 20, "bold"))],
    [sg.T("",size=(1,1),font=("Any",))],

    [sg.P(),sg.Frame("",[[sg.Text("Título")], [sg.Input('Tarefa ', key="-TITULO-")],
    [sg.Text("Descrição")], [sg.Multiline('Descrição da Tarefa', key="-DESC-", size=(43, 5))],
    [sg.Text("Data Limite")], [sg.Input('Data Limite (AAAA-MM-DD)', key="-DATA-")],
    [sg.Text("Prioridade")],
    [sg.Radio('Alta', 'PRIORIDADE', key='-ALTA-', default=True), 
     sg.Radio('Média', 'PRIORIDADE', key='-MEDIA-'), 
     sg.Radio('Baixa', 'PRIORIDADE', key='-BAIXA-')],
    [sg.Text("ID Atividade")], [sg.Input('', key="-ID-", size=(5,1)),sg.Checkbox("Concluida", key="-SN-")],
    [sg.Button('Adicionar Tarefa'), sg.P(),sg.Button('Atualizar Tarefa'),sg.P(), sg.Button('Excluir Tarefa')]]),sg.P()],
    
    [sg.P(),sg.Frame("",[[sg.Text("Pesquisar por ID")], [sg.Input('', key="-SEARCH_ID-", size=(5,1)),sg.T("",size=(19,1)), sg.Button('Pesquisar Tarefa')]]),sg.P()],
    [sg.Button('Sair',size=(5,1),button_color='red')],
]

col2 = [
    [sg.Multiline('', key='tarefas', size=(53, 30))],
    
]

layout = [
    [sg.TabGroup([
        [sg.Tab("TAREFAS", col)],
        [sg.Tab("POSTITS", col2)]
    ])]
]

window = sg.Window('Gerenciador de Tarefas', layout, )

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
            atualizar_tarefas(prioridade)
            # Atualizar a lista de tarefas no segundo tab (POSTITS)
            atualize()
            

    elif event == 'Pesquisar Tarefa':
        buscar_id = int(values['-SEARCH_ID-']) if values['-SEARCH_ID-'].isdigit() else None
        if buscar_id is None:
            sg.popup("Digite um ID válido para pesquisar!")
        else:
            found_task = next((tarefa for tarefa in tarefas_postits if tarefa['Id'] == buscar_id), None)
            if found_task:
                status = found_task['Prioridade']
                print(status)
                window['-ID-'].update(found_task['Id'])
                window['-TITULO-'].update(found_task['Titulo'])
                window['-DESC-'].update(found_task['Descricao'])
                window['-DATA-'].update(found_task['Prazo'])
                window['-ALTA-'].update(value=found_task['Prioridade'] == 'Alta')
                window['-MEDIA-'].update(value=found_task['Prioridade'] == 'Media')
                window['-BAIXA-'].update(value=found_task['Prioridade'] == 'Baixa')
                window['-SN-'].update(found_task['Concluida'])
            else:
                sg.popup(f"Tarefa com ID {buscar_id} não encontrada!")

    
    elif event == 'Excluir Tarefa':
        buscar_id = int(values['-SEARCH_ID-']) if values['-SEARCH_ID-'].isdigit() else None
        if buscar_id is None:
            sg.popup("Digite um ID válido para pesquisar!")

        else: # Verifica se a tarefa com o ID fornecido existe
            found_task = next((tarefa for tarefa in tarefas_postits if tarefa['Id'] == buscar_id), None)
            if found_task is not None:
                tarefas_postits.remove(found_task)
                sg.popup(f"Tarefa com ID {buscar_id} foi removida")

            else:
                sg.popup(f"Nenhuma tarefa encontrada com o ID {buscar_id}")
        atualize()
            
    elif event == 'Atualizar Tarefa':
        search_id = int(values['-SEARCH_ID-'])
        if not values['-TITULO-'] or not values['-DESC-'] or not values['-DATA-'] or not values['-ID-']:
            sg.popup("Preencha todos os campos!")
        else:
            # Determinar a prioridade
            if values['-ALTA-']:
                prioridade = 'Alta'
            elif values['-MEDIA-']:
                prioridade = 'Média'
            else:
                prioridade = 'Baixa'
            
            # Encontrar a tarefa pelo ID
            
            found_task = next((tarefa for tarefa in tarefas_postits if tarefa['Id'] == search_id), None)

            if found_task:
                # Atualizar os campos da tarefa encontrada
                found_task['Titulo'] = values['-TITULO-']
                found_task['Descricao'] = values['-DESC-']
                found_task['Prazo'] = values['-DATA-']
                found_task['Prioridade'] = prioridade
                found_task['Concluida'] = values['-SN-']
                
                # Atualizar a lista de tarefas na interface
                task_list_content = ""
                for tarefa in tarefas_postits:
                    concluida = "Sim" if tarefa["Concluida"] else "Não"
                    task_list_content += f"ID: {tarefa['Id']}\nTítulo: {tarefa['Titulo']}\nDescrição: {tarefa['Descricao']}\nData Limite: {tarefa['Prazo']}\nConcluída: {concluida}\nPrioridade: {tarefa['Prioridade']}\n\n"
                window['tarefas'].update(task_list_content)
                
                sg.popup(f"Tarefa com ID {search_id} foi atualizada com sucesso!")
            else:
                sg.popup(f"Tarefa com ID {search_id} não encontrada!")

window.close()


