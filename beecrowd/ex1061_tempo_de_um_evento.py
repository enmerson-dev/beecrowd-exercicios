# Horário Entrada da festa
diaE = int(input().split()[1])
horarioE = input().split(':')
horaE = int(horarioE[0])
minutoE = int(horarioE[1])
segundoE = int(horarioE[2])

# Horário Saída da festa
diaS = int(input().split()[1])
horarioS = input().split(':')
horaS = int(horarioS[0])
minutoS = int(horarioS[1])
segundoS = int(horarioS[2])

tempoE = diaE * 86400 + horaE * 3600 + minutoE * 60 + segundoE
tempoS = diaS * 86400 + horaS * 3600 + minutoS * 60 + segundoS

duracao = tempoS - tempoE

dia = duracao // 86400
duracao %= 86400
hora = duracao // 3600
duracao %= 3600
minuto = duracao // 60
segundo = duracao % 60

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundo} segundo(s)')