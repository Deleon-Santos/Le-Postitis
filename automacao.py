import win32com.client as win32


outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = 'delps.santos1987@gmail.com'
email.Subject = "Tarefas adicionadas"
email.HTMLBody = f'''
<p>Lista de Terefas Adicionadas</p>

<p> </p>

<p> </p>'''
print("Email enviado com successo.")
email.Send()