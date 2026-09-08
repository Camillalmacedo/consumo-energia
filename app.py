aparelho = input("Digite o nome do aparelho: ")
potencia = int(input("Digite a potência do aparelho em watts (W): "))
tempo_medio = int(input("Digite o tempo médio de uso diário em horas: "))
consumo_mensal = (potencia * tempo_medio * 30) / 1000
custo = consumo_mensal * 0.75  # Supondo que o custo por kWh seja R$ 0,75


print(f''' 
Aparelho: {aparelho}
Consumo estimado: {consumo_mensal}
Custo estimado: R$ {custo:.2f}

''')