import pyodbc
from random import randint
dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-CNOFHH8;"
    "DATABASE=Barbearia;"
)
conexao = pyodbc.connect(dados_conexao)
print('Conexão realizada!')
print()

cursor = conexao.cursor()
def cadastro():
    idUsers = []
    idUsuario = randint(1, 1000)
    idUsers.append(idUsuario)
    while idUsuario == idUsers:
        idUsuario = randint(1, 1000)
    idUsers.append(idUsuario)
    print()
    email = (input('Digite seu e-mail: '))
    senha = (input('Crie sua senha: '))
    nome = (input('Nome de usuario: '))
    cursor.execute(f"""INSERT INTO usuario (idUsuario,email,senha,nome) 
                   VALUES ('{idUsuario}','{email}','{senha}','{nome}')""")
    
    conexao.commit()
    print('Cadastro realizado com sucesso!')
    print()

def login():
    # Conectar ao banco de dados
    dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-CNOFHH8;"
    "DATABASE=Barbearia;"
    )
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    email = input('Digite seu e-mail: ')
    senha = input('Digite sua senha: ')
    # Verificar se o email e senha correspondem a um usuário registrado
    cursor.execute(f"SELECT * FROM usuario WHERE email = '{email}' AND senha = '{senha}'")
    usuario = cursor.fetchone()

    if usuario:
        print('Login bem-sucedido!')
        marcar()
        # Aqui você pode adicionar qualquer lógica adicional que deseja executar após o login ser bem-sucedido
    else:
        print('E-mail ou senha incorretos. Tente novamente.')
        login()
    conexao.close()
    print()

def marcar():
    dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-CNOFHH8;"
    "DATABASE=Barbearia;"
    )
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    agenda = []
    idAgenda = randint(1, 1000)
    agenda.append(idAgenda)
    while idAgenda == agenda:
        idAgenda = randint(1, 1000)
    agenda.append(idAgenda)
    print()
    nome = input('Digite seu nome: ')
    print(f'Muito bem {nome}, agora escolha o horário!')
    print()
    with open('horariosIndisponiveis.txt', 'r', encoding="utf-8" , errors="ignore") as ler:
        visualizar = ler.readlines()
        if visualizar:
            print()
            for linha in visualizar:
                print(linha.strip()) 
        else:
            print('Nenhum horário indisponível encontrado.')     
    print()
    dias = {
    '1': 'Segunda-Feira',
    '2': 'Terça-Feira',
    '3': 'Quarta-Feira',
    '4': 'Quinta-Feira',
    '5': 'Sexta-Feira',
    '6': 'Sábado',
}

    data = input('''Escolha o dia.
    1 - Segunda-Feira
    2 - Terça-Feira
    3 - Quarta-Feira
    4 - Quinta-Feira
    5 - Sexta-Feira
    6 - Sábado
    : ''')

    if data in dias:
        dia_escolhido = dias[data]
    else:
        print('Opção de dia inválida.')
    # Aqui você pode decidir se deseja sair do programa ou lidar com o erro de outra forma
        exit()

    horarios = {
        '1': '08:00',
        '2': '09:00',
        '3': '10:00',
        '4': '11:00',
        '5': '12:00',
        '6': '14:00',
        '7': '15:00',
    }

    print()
    horario = input('''Escolha o horário
    1 - 08:00
    2 - 09:00
    3 - 10:00
    4 - 11:00
    5 - 12:00
    6 - 14:00
    7 - 15:00
    : ''')

    if horario in horarios:
        horario_escolhido = horarios[horario]
    else:
        print('Opção de horário inválida.')
    # Aqui você pode decidir se deseja sair do programa ou lidar com o erro de outra forma
    cursor.execute(f"SELECT * FROM agenda WHERE horario = '{horario_escolhido}' AND data_corte = '{dia_escolhido}'")
    agenda = cursor.fetchone()

    if not agenda:
        print('Horário marcado com sucesso!')
        cursor.execute(f"""INSERT INTO agenda (idAgenda, nome, horario, data_corte) VALUES ('{idAgenda}', '{nome}', '{horario_escolhido}', '{dia_escolhido}')""")
        conexao.commit()
        print(f'Muito bem {nome}, processo finalizado. O seu número da agenda é {idAgenda}, guarde-o caso queira remarcar.')
        print('Horário marcado com sucesso, esperamos por você!')
        with open('horariosIndisponiveis.txt', 'a+', encoding='utf-8') as arquivo:
            arquivo.write(f'O Horário escolhido {horario_escolhido} na(o) {dia_escolhido} está indisponível.\n')
        print()
        # Aqui você pode adicionar qualquer lógica adicional que deseja executar após o horário ser marcado com sucesso
    else:
        print('Horário indisponível. Tente novamente.')
    # Se desejar, pode chamar a função marcar() para tentar novamente
        marcar()
        print()

def remarcar():
    dados_conexao = (
        "DRIVER={SQL Server};"
        "SERVER=DESKTOP-CNOFHH8;"
        "DATABASE=Barbearia;"
    )
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    nome = input('Digite seu nome: ')
    with open('horariosIndisponiveis.txt', 'r', encoding="utf-8", errors="ignore") as ler:
        visualizar = ler.readlines()
        if visualizar:
            print()
            for linha in visualizar:
                print(linha.strip())
        else:
            print('Nenhum horário indisponível encontrado.')
    print()

    dias = {
        '1': 'Segunda-Feira',
        '2': 'Terça-Feira',
        '3': 'Quarta-Feira',
        '4': 'Quinta-Feira',
        '5': 'Sexta-Feira',
        '6': 'Sábado',
    }
    data = input('''Escolha o dia.
1 - Segunda-Feira
2 - Terça-Feira
3 - Quarta-Feira
4 - Quinta-Feira
5 - Sexta-Feira
6 - Sábado
: ''')
    if data in dias:
        novo_dia = dias[data]
    else:
        print('Opção de dia inválida. Escolha novamente')
        remarcar()
        return

    print()
    horarios = {
        '1': '08:00',
        '2': '09:00',
        '3': '10:00',
        '4': '11:00',
        '5': '12:00',
        '6': '13:00',
        '7': '14:00',
    }
    horario = input('''Escolha o horário
1 - 08:00
2 - 09:00
3 - 10:00
4 - 11:00
5 - 12:00
6 - 14:00
7 - 15:00
: ''')
    if horario in horarios:
        novo_horario = horarios[horario]
    else:
        print('Opção de horário inválida.')
        return

    id_agenda = input('Digite o ID da agenda a ser remarcada: ')

    cursor.execute("SELECT * FROM agenda WHERE idAgenda = ?", id_agenda)
    agenda_existente = cursor.fetchone()

    if agenda_existente:
        # Se a agenda existe, atualize os dados
        try:
            cursor.execute("UPDATE agenda SET nome = ?, horario = ?, data_corte = ? WHERE idAgenda = ?", nome, novo_horario, novo_dia, id_agenda)
            conexao.commit()
            print('Agenda remarcada com sucesso no banco de dados!')
        except pyodbc.Error as ex:
            print('Erro ao atualizar a agenda no banco de dados:', ex)
            print('Não foi possível remarcar a agenda. Tente novamente.')
    else:
       pass

    # Atualizar o arquivo de texto com a nova informação
    with open('horariosIndisponiveis.txt', 'r', encoding="utf-8", errors="ignore") as arquivo_leitura:
        linhas = arquivo_leitura.readlines()

    with open('horariosIndisponiveis.txt', 'w', encoding="utf-8", errors="ignore") as arquivo_escrita:
        for linha in linhas:
            if f'ID da Agenda: {id_agenda}' in linha:
                arquivo_escrita.write(f'O Horário escolhido {novo_horario} na(o) {novo_dia} está indisponível.\n')
                print()
                print('Agenda remarcada com sucesso no arquivo de texto!')
            else:
                arquivo_escrita.write(linha)

    conexao.close()

while True:
    menu = int(input('''
    Escolha uma opção      
    1. Cadastro
    2. Login
    3. Remarcar
    4. Sair
    : '''))

    if menu == 1:
        cadastro()
    elif menu == 2:
        login()
    elif menu == 3:
        remarcar()
    elif menu == 4:
        break;
    elif menu >= 5:
        print('Opção inválida.') 