# RADAR ELETRONICO VALOR DA MULTA R$5,00 POR CADA KM ACIMA DO LIMITE!

velocidaide = float(input("Qual a velocidade atual do Carro?  "))
if velocidaide > 80:
    print('MULTADO! VOCÊ EXCEDEU O LIMITE PERMITIDO QUE É DE 80Km/h')
    multa = (velocidaide - 80) * 5
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

else:
    print('Tenha um Bom Dia! DIRIGA COM SEGURANÇA')





