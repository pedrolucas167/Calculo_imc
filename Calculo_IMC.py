while True:
    try:
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura: '))
    except ValueError:
        print('Digite valores numéricos válidos para peso e altura.')
        continue
        
    imc = peso / altura ** 2
    imc = round(imc, 1)
   

    print('Seu IMC é {:.1f}'.format(imc))
    if imc < 18.5:
        print('Você está abaixo do peso ideal.')
    elif 18.5 <= imc < 25:
        print('Você está no peso ideal.')
    elif 25 <= imc < 30:
        print('Você está com sobrepeso.')
    else:
        print('Você está obeso.')
    break