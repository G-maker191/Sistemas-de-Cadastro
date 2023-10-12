from PySimpleGUI import PySimpleGUI as sg
import mysql.connector

connect = mysql.connector.connect(host='localhost',user='root',password='root',database='clientes')

cursor = connect.cursor()
sg.theme('reddit')

layout = [
        [sg.Text('Nome'),sg.Input(key='nome')],
        [sg.Text('Email'),sg.Input(key='email')],
        [sg.Text('CPF'),sg.Input(key='cpf')],
        [sg.Button('Cadastrar')]

]

janela = sg.Window('Cadastro de Cliente',layout)

while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
            break
    if eventos == 'Cadastrar':
        nome = valores['nome']
        cpf = valores['cpf']
        email = valores['email']
        comand = f'INSERT INTO cliente(nome,cpf,email) VALUES ("{nome}","{cpf}","{email}")'
        cursor.execute(comand)
        connect.commit()

    comandRead = f'SELECT * from cliente'
    cursor.execute(comandRead)
    resultado = cursor.fetchall()
    print(resultado)




    cursor.close()
    connect.close()