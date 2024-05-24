import PySimpleGUI as sg


tarefas_postits = []
id_contador = 0


def atualizar_tarefas(prioridade,concluida):
    global id_contador
    
    id_contador += 1
    tarefa = {
        "Id": id_contador,
        "Titulo": values['-TITULO-'],
        "Descricao": values['-DESC-'],
        "Prazo": values['-DATA-'],
        "Prioridade": prioridade,
        "Concluida": values['-SN-']}
        
    tarefas_postits.append(tarefa)      
    sg.popup("Tarefa Agendada")

def atualize():
        lista_tarefas = ''
        for tarefa in tarefas_postits:          
            lista_tarefas += f"ID: {tarefa['Id']}\nTítulo: {tarefa['Titulo']}\nDescrição: {tarefa['Descricao']}\nData Limite: {tarefa['Prazo']}\nConcluída: {'Sim' if tarefa['Concluida']== True else 'Não'}\nPrioridade: {tarefa['Prioridade']}\n\n"
        
        window['tarefas'].update(lista_tarefas)
        print(lista_tarefas)
        



sg.SetOptions(
                background_color='#363636', 
                text_element_background_color='#363636',
                element_background_color='#363636', 
                scrollbar_color=None, input_elements_background_color='#F7F3EC', 
                button_color=('white', '#4F4F4F'))#Configuração de thema da janela

# Criar interface gráfica
esquerda=[
    [sg.Image(filename='img.png',size=(450,650))]]
col = [
    [sg.T("",size=(1,1),font=("Any",1))],
    [sg.Text('GERENCIADOR DE TAREFAS', font=("Any", 20, "bold"))],
    [sg.T("",size=(1,1),font=("Any",))],

    [sg.P(),sg.Frame("Adição de Tarefas",[[sg.Text("Título")], [sg.Input('Tarefa ', key="-TITULO-")],
    [sg.Text("Descrição")], [sg.Multiline('Devo me Lembrar!', key="-DESC-", size=(43, 5))],
    [sg.Text("Data Limite")], [sg.CalendarButton("Escolher Data", target='-DATA-', format='%d/%m/%Y'),sg.Input('10/12/2024' ,key="-DATA-",size=(18,1))],
    
    [sg.Text("Prioridade")],
    [sg.Radio('Alta', 'PRIORIDADE', key='-ALTA-'), 
     sg.Radio('Média', 'PRIORIDADE', key='-MEDIA-'), 
     sg.Radio('Baixa', 'PRIORIDADE', key='-BAIXA-', default=True)],
    
    [sg.Text("ID Atividade")], [sg.Input('', key="-ID-", size=(5,1)),sg.Checkbox("Concluida", key="-SN-")],
    [sg.Button('Adicionar Tarefa'), sg.P(),sg.Button('Atualizar Tarefa'),sg.P(), sg.Button('Excluir Tarefa')]]),sg.P()],
    
    [sg.P(),sg.Frame("Pesquisa",[[sg.Text("Pesquisar por ID")], [sg.Input('', key="-SEARCH_ID-", size=(5,1)),sg.T("",size=(19,1)), sg.Button('Pesquisar Tarefa')]]),sg.P()],
    [sg.Button('Sair',size=(5,1),button_color='red')],]

col2 = [
    [sg.Multiline('', key='tarefas', size=(53, 30))],
    [sg.Frame("Pesquisa por Estado",[[sg.Text("Prioridade",size=(48,1))],[sg.Radio('Alta', 'PRIORIDAD', key='-TALTA-', default=True), sg.Radio('Média', 'PRIORIDAD', key='-TMEDIA-'),
    sg.Radio('Baixa', 'PRIORIDAD', key='-TBAIXA-'),sg.Checkbox("Concluidas", key="-TSN-"),sg.Push(),sg.B('Buscar')]])],
    [sg.Button("Listar Tarefas")],]
direita=[
     [sg.TabGroup([
        [sg.Tab("TAREFAS", col)],
        [sg.Tab("POSTITS", col2)]])]]


layout = [
    [sg.Col(esquerda),
    sg.Col(direita)]]

window = sg.Window('Gerenciador de Tarefas', layout,size=(930,650),resizable=True )
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    elif event == 'Adicionar Tarefa':
        if not values['-TITULO-'] or not values['-DESC-'] or not values['-DATA-']:
            sg.popup("Preencha todos os campos!")
        
        else:
            concluida= 'Sim' if values['-SN-']==True else 'Não'
            prioridade = "Alta" if values['-ALTA-'] else "Medio" if values['-MEDIA-'] else "Baixo"
            atualizar_tarefas(prioridade,concluida)
            atualize()
        
    elif event == 'Pesquisar Tarefa':
        buscar_id = int(values['-SEARCH_ID-']) if values['-SEARCH_ID-'].isdigit() else None
        if buscar_id is None:
            sg.popup("Digite um ID válido para pesquisar!")
        
        else:
            lista_atualizar = next((tarefa for tarefa in tarefas_postits if tarefa['Id'] == buscar_id), None)
            if lista_atualizar:
                status = lista_atualizar['Prioridade']
                print(status)
                window['-ID-'].update(lista_atualizar['Id'])
                window['-TITULO-'].update(lista_atualizar['Titulo'])
                window['-DESC-'].update(lista_atualizar['Descricao'])
                window['-DATA-'].update(lista_atualizar['Prazo'])
                window['-ALTA-'].update(value=lista_atualizar['Prioridade'] == 'Alta')
                window['-MEDIA-'].update(value=lista_atualizar['Prioridade'] == 'Media')
                window['-BAIXA-'].update( value=lista_atualizar['Prioridade'] == 'Baixa')
                window['-SN-'].update(lista_atualizar['Concluida'])
                print(lista_atualizar['Concluida'])
            
            else:
                sg.popup(f"Tarefa com ID {buscar_id} não encontrada!")

    elif event == 'Excluir Tarefa':
        buscar_id = int(values['-SEARCH_ID-']) if values['-SEARCH_ID-'].isdigit() else None
        if buscar_id is None:
            sg.popup("Digite um ID válido para pesquisar!")

        else: # Verifica se a tarefa com o ID fornecido existe
            lista_excluir = next((tarefa for tarefa in tarefas_postits if tarefa['Id'] == buscar_id), None)
            if lista_excluir is not None:
                tarefas_postits.remove(lista_excluir)
                sg.popup(f"Tarefa com ID {buscar_id} foi removida")
            
            else:
                sg.popup(f"Nenhuma tarefa encontrada com o ID {buscar_id}")
        atualize()
            
    elif event == 'Atualizar Tarefa':
        search_id = int(values['-SEARCH_ID-'])
        if not values['-TITULO-'] or not values['-DESC-'] or not values['-DATA-'] or not values['-ID-']:
            sg.popup("Preencha todos os campos!")
        
        else:
            prioridade = "Alta" if values['-ALTA-'] else "Medio" if values['-MEDIA-'] else "Baixo"
            
            # Encontrar a tarefa pelo ID
            lista_atualizada = next((tarefa for tarefa in tarefas_postits if tarefa['Id'] == search_id), None)
            if lista_atualizada:
                lista_atualizada['Titulo'] = values['-TITULO-']
                lista_atualizada['Descricao'] = values['-DESC-']
                lista_atualizada['Prazo'] = values['-DATA-']
                lista_atualizada['Prioridade'] = prioridade
                lista_atualizada['Concluida'] = values['-SN-']
                
                # Atualizar a lista de tarefas na interface
                atualize()
                sg.popup(f"Tarefa com ID {search_id} foi atualizada com sucesso!")
            else:
                sg.popup(f"Tarefa com ID {search_id} não encontrada!")
    
    elif event == "Buscar":
        checkbox = values['-TSN-']
        prioridad = "Alta" if values['-TALTA-'] else "Medio" if values['-TMEDIA-'] else "Baixo"
        
        task_mostar = ""
        
        for tarefa in tarefas_postits:
            if tarefa['Prioridade'] == prioridad and tarefa['Concluida'] == checkbox:
                task_mostar += f"ID: {tarefa['Id']}\nTítulo: {tarefa['Titulo']}\nDescrição: {tarefa['Descricao']}\nData Limite: {tarefa['Prazo']}\nConcluída: {'Sim'if tarefa['Concluida']==True else 'Não'}\nPrioridade: {tarefa['Prioridade']}\n\n"
        
        if task_mostar:
            window['tarefas'].update(task_mostar)
            print(f'lista de tarefas{task_mostar}')
        else:
            window['tarefas'].update(task_mostar)
            sg.popup("Nenhuma tarefa encontrada com os critérios selecionados!")
    elif event == 'Listar Tarefas':
        atualize()
        

window.close()


