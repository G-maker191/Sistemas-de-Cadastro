import mysql.connector
from PySimpleGUI import PySimpleGUI as sg


connect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clientes'

)

cursor = connect.cursor()


sg.theme('reddit')

layout = [
    [sg.Text('Nome'),sg.Input(key='nome')],
    [sg.Text('Email'),sg.Input(key='email')],
    [sg.Text('Senha(CPF)'),sg.Input (key='senha',password_char='*')],
    [sg.Button('Logar')]


]

janela = sg.Window('Login',layout)

while True:
    values,events = janela.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Logar':
        nome = values['nome']
        senha = values['senha']
        email = values['email']
        comand = f'SELECT * from cliente'
        cursor.execute(comand)

    resultado = cursor.fetchall()

