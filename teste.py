horarios_disponiveis = {
    '1': '08:00',
    '2': '09:00'
}

agenda = []

while True:
    print("Horários disponíveis:")
    for chave, valor in horarios_disponiveis.items():
        if valor not in agenda:
            print(f"{chave}: {valor}")

    horario = input('Escolha o horário (ou digite "S" para sair): ')
    if horario.lower() == 's':
        break

    if horario in horarios_disponiveis and horarios_disponiveis[horario] not in agenda:
        horario_escolhido = horarios_disponiveis[horario]
        agenda.append(horario_escolhido)
        print(f"Você escolheu o horário: {horario_escolhido}")
    else:
        print('Opção de horário inválida ou horário já agendado. Escolha outro horário.')

print("Agenda finalizada. Horários agendados:")
print(agenda)