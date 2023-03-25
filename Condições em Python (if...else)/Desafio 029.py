velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade-80)*7
if velocidade >= 80:
    print('\033[31mMULTADO! Você exceu o limite permitido que é de 80km/h \033[m')
    print('\033[31mVocê deve pagar uma multa de\033[m \033[33mR${:.2f}\033[m'.format(multa))
else:
    print('\033[32m Tenha um bom dia! Dirija com segurança!\033[m')