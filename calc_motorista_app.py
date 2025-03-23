
# Objetivo do projeto: desenvolver uma calculadora
# de custos operacionais relacionados ao trabalho
# de motorista de aplicativo.


# Ambiente 1 - O programa recebe as informacoes do usuario

print(''' Ola! Essa ferramenta te auxiliara a extrair
 o lucro liquido do seu trabalho na data de hoje!''')

nome_usuario = str(input(' Insira seu nome: ')).strip().title()

print(f'\n Seja Bem-Vindo(a) {nome_usuario} ! E muito gratificante ter voce!')

print('''\n Agora, precisamos que voce nos informe os
 detalhes do seu expediente para apresentarmos a sua performance:''')

nome_veiculo = str(input('\n Insira o nome do veiculo: ')).strip().title()

placa_veiculo = str(input('''\n Insira a placa do veiculo 
 (XXX-1234 / XXX-12A4): ''')).strip().upper()

data_expediente = str(input('''\n Insira a data do expediente
 (DD/MM/AAAA): ''')).strip()

ganho_total = float(input('''\n Insira sua receita
 total do dia: ''').replace(',', '.'))

horas_expediente = float(input('''\n Insira o tempo
 online (horas): ''').replace(',', '.'))

km_percorrido = float(input('''\n Insira a quilometragem
 percorrida no total: ''').replace(',', '.'))

tipo_combustivel = str(input('''\n Insira qual combustivel
 foi utilizado: '''))

litros_combustivel = float(input('''\n Insira a qtde de combustivel 
 utilizada (litros): ''').replace(',', '.'))

preco_combustivel = float(input('''\n Insira o preco
 do combustivel: ''').replace(',', '.'))


custo_km_rodado = float(input("""\n Insira seu custo
 fixo por quilometro rodado: """).replace(',', '.'))

custo_por_hora = float(input("""\n Insira seu custo fixo
 por hora: """).replace(',', '.'))

print('=' * 20)

print(f'''\n \033[1;32;40m{nome_usuario}, agora com essas informações e
 possivel te apresentar alguns dados! Confira:\033[0m''')

print('\n')
print('=' * 20)

print(f'\n Informacoes do condutor: {nome_usuario}')
print(f'\n O veiculo utilizado e {nome_veiculo} de placa: {placa_veiculo}.')

print(f'\n A data do expediente informado e: {data_expediente}')

print('\n')
print('=' * 20)

# Ambiente 2 - calculo:

ganho_km = float(ganho_total / km_percorrido)

print(f'\n Seu ganho bruto por quilometro rodado e: {ganho_km:.2f} R$/km!')

ganho_hora = float(ganho_total / horas_expediente)

print(f'\n Seu ganho bruto por hora e: {ganho_hora:.2f} R$/h!')

custo_combustivel = float(litros_combustivel * preco_combustivel)

autonomia_km = float(km_percorrido / litros_combustivel)

print(f'''\n Seu custo com combustivel foi
 de: \033[1;31;40mR$ {custo_combustivel:.2f}\033[0m''')

print(f'''\n A autonomia do veiculo por
 quilometro rodado foi de: {autonomia_km:.2f} km/l!''')

custo_km_combustivel = float(custo_combustivel / km_percorrido)

print(f'''\n O seu custo de combustivel por quilometro rodado
 e de: \033[1;31;40m{custo_km_combustivel:.2f} R$/km!\033[0m''')

ganho_liquido = float(ganho_total - custo_combustivel)

km_liquido = float(ganho_liquido / km_percorrido)

hora_liquido = float(ganho_liquido / horas_expediente)

custo_total_hora = horas_expediente * custo_por_hora

custo_total_km_rodado = km_percorrido * custo_km_rodado

ganho_real = (
    ganho_total - custo_combustivel
    - custo_total_hora - custo_total_km_rodado
    )

ganho_hora_real = ganho_real / horas_expediente

ganho_km_real = ganho_real / km_percorrido

custo_total = (
    custo_combustivel + custo_total_km_rodado +
    custo_total_hora
    )

# Ambiente 3 - O programa apresenta os resultados

print(f'''\n O ganho liquido hoje
 foi de: \033[1;32;40mR$ {ganho_liquido:.2f}\033[0m!
 Parabens pelo seu resultado!
 Continue buscando por seus objetivos!''')

print(f'''\n O seu ganho liquido por quilometro rodado e
 de \033[1;32;40m{km_liquido:.2f} R$/km!\033[0m''')

print(f'''\n O seu ganho liquido por
 hora e: \033[1;32;40m{hora_liquido:.2f} R$/h!\033[0m''')

print('''\n Agora segue o seu ganho real,
 considerando os custos:
      
     *Custo fixo por quilometro rodado
     *Custo fixo por hora trabalhada
     *Custo de combustivel: ''')

print('\n')
print('='*20)

print(f'\n O seu ganho por hora real e de: R$ {ganho_hora_real:.2f}/h')

print(f'''\n O seu ganho real por quilometro
 rodado e R$ {ganho_km_real:.2f}/km.''')

print(f'''\n O seu Custo total por km fixo (R$0,21/km)
 e de R$ {custo_total_km_rodado:.2f}''')

print(f'\n O seu Custo total por hora e de R$ {custo_total_hora:.2f}.')

print(f' O seu custo total e de R${custo_total:.2f}.')

print('\n')
print('=' * 20)

print(f'''\n O seu acumulado real excluido
 todos os custos e de R$ {ganho_real:.2f}.''')

print('''\n Obrigado por utilizar nosso programa
 para calcular seu lucro! Ate a proxima!''')
