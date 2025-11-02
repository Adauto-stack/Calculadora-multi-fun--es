import math
import os
comando_limpeza = 'cls' if os.name == 'nt' else 'clear'
print('Bem Vindo A Calculadora Python \nPressione ENTER para continuar')
input()
while True:
    os.system(comando_limpeza)
    print('Escolha a operação que deseja realizar: \n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potenciação\n[6] Raiz Quadrada\n[7] outro \n[8] sair ')
    escolha = input('Digite a opção desejada: ')
    if escolha == '1':
        os.system(comando_limpeza)
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = num1 + num2
        print(f'O resultado da soma é: {resultado}')
        input('Pressione ENTER para continuar')
    elif escolha == '2':
        os.system(comando_limpeza)
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = num1 - num2
        print(f'O resultado da subtração é: {resultado}')
        input('Pressione ENTER para continuar')
    elif escolha == '3':
        os.system(comando_limpeza)
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = num1 * num2
        print(f'O resultado da multiplicação é: {resultado}')
        input('Pressione ENTER para continuar')
    elif escolha == '4':
        os.system(comando_limpeza)
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        if num2 == 0:
            print('Erro: Divisão por zero não é permitida.')
        else:
            resultado = num1 / num2
            print(f'O resultado da divisão é: {resultado}')
        input('Pressione ENTER para continuar')
    elif escolha == '5':
        os.system(comando_limpeza)
        num1 = float(input('Digite a base: '))
        num2 = float(input('Digite o expoente: '))
        resultado = num1 ** num2
        print(f'O resultado da potenciação é: {resultado}')
        input('Pressione ENTER para continuar')
    elif escolha == '6':
        os.system(comando_limpeza)
        num = float(input('Digite o número para calcular a raiz quadrada: '))
        if num < 0:
            print('Erro: Não é possível calcular a raiz quadrada de um número negativo.')
        else:
            resultado = math.sqrt(num)
            print(f'O resultado da raiz quadrada é: {resultado}')
        input('Pressione ENTER para continuar')
    elif escolha == '7':
        while True:
            os.system(comando_limpeza)
            print('Escolha a operação personalizada: \n[1] Conversão de moedas\n[2] Cálculo de IMC \n[3] Km/h para m/s e m/s para km/h \n[4] Celsius para Fahrenheit e Fahrenheit para Celsius \n[5] Tabuada \n[6] Voltar para o menu principal')
            opcao = input('Digite a opção desejada: ')
            os.system(comando_limpeza)
            if opcao == '1':
                while True:
                    os.system(comando_limpeza)
                    print('Escolha a conversão de moedas: \n[1] Real para Dólar \n[2] Dólar para Real \n[3] Euro para Real \n[4] Real para Euro \n[5] Voltar')
                    moeda = input('Digite a opção desejada: ')
                    if moeda == '1':
                        os.system(comando_limpeza)
                        real = float(input('Digite o valor em reais: '))
                        conversao = real / 5.38
                        print(f'R$ {real} equivalem a US$ {conversao:.2f}')
                        input('Pressione ENTER para continuar')
                    elif moeda == '2':
                        os.system(comando_limpeza)
                        dolar = float(input('Digite o valor em dólares: '))
                        conversao = dolar * 5.38
                        print(f'US$ {dolar} equivalem a R$ {conversao:.2f}')
                        input('Pressione ENTER para continuar')
                    elif moeda == '3':
                        os.system(comando_limpeza)
                        euro = float(input('Digite o valor em euros: '))
                        conversao = euro * 6.25
                        print(f'€ {euro} equivalem a R$ {conversao:.2f}')
                        input('Pressione ENTER para continuar')
                    elif moeda == '4':
                        os.system(comando_limpeza)
                        real = float(input('Digite o valor em reais: '))
                        conversao = real / 6.25
                        print(f'R$ {real} equivalem a € {conversao:.2f}')
                        input('Pressione ENTER para continuar')
                    elif moeda == '5':
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
            elif opcao == '2':
                os.system(comando_limpeza)
                peso = float(input('Digite seu peso em kg: '))
                altura = float(input('Digite sua altura em metros: '))
                imc = peso / (altura ** 2)
                print(f'Seu IMC é: {imc:.2f}')
                input('Pressione ENTER para continuar')
            elif opcao == '3':
                os.system(comando_limpeza)
                velocidade = float(input('Digite a velocidade: '))
                unidade = input('Digite a unidade (km/h ou m/s): ')
                if unidade == 'km/h':
                    conversao = velocidade / 3.6
                    print(f'{velocidade} km/h equivalem a {conversao:.2f} m/s')
                elif unidade == 'm/s':
                    conversao = velocidade * 3.6
                    print(f'{velocidade} m/s equivalem a {conversao:.2f} km/h')
                else:
                    print('Unidade inválida.')
                os.system(comando_limpeza)
                input('Pressione ENTER para continuar')
            elif opcao == '4':
                os.system(comando_limpeza)
                celcius_fahrenheit = input('Escolha qual conversão deseja fazer: \n[1] Celsius para Fahrenheit \n[2] Fahrenheit para Celsius \nDigite a opção desejada: ')
                if celcius_fahrenheit == '1':
                    os.system(comando_limpeza)
                    celcius = float(input('Digite a temperatura em Celsius: '))
                    graus_fahrenheit = (celcius * 1.8) + 32
                    print(f'{celcius}°C equivalem a {graus_fahrenheit:.2f}°F')
                elif celcius_fahrenheit == '2':
                    os.system(comando_limpeza)
                    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
                    graus_celcius = (fahrenheit - 32) / 1.8
                    print(f'{fahrenheit}°F equivalem a {graus_celcius:.2f}°C')
                else:
                    os.system(comando_limpeza)
                    print('Opção Inválida.')
                input('Pressione ENTER para continuar')
            elif opcao == '5':
                while True:
                    operacao = input('Escolha a operação da tabuada: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \n[5] Sair \nDigite a opção desejada: ')
                    os.system(comando_limpeza)
                    if operacao == '1':
                        os.system(comando_limpeza)
                        numero = int(input('Digite o número para a tabuada: '))
                        for i in range(1, 11):
                            print(f'{numero} + {i}= {numero + i}')
                        input('Pressione ENTER para continuar')
                    elif operacao == '2':
                        os.system(comando_limpeza)
                        numero = int(input('Digite o número para a tabuada: '))
                        for i in range(1, 11):
                            print(f'{numero} - {i}= {numero - i}')
                        input('Pressione ENTER para continuar')
                    elif operacao == '3':
                        os.system(comando_limpeza)
                        numero = int(input('Digite o número para a tabuada: '))
                        for i in range(1, 11):
                            print(f'{numero} x {i}= {numero * i}')
                        input('Pressione ENTER para continuar')
                    elif operacao == '4':
                        os.system(comando_limpeza)
                        numero = int(input('Digite o número para a tabuada: '))
                        for i in range(1, 11):
                            if i == 0:
                                print(f'{numero} / {i}= Indefinido (divisão por zero)')
                            else:
                                print(f'{numero} / {i}= {numero / i}')
                        input('Pressione ENTER para continuar')
                    elif operacao == '5':
                        break
                    else:
                        os.system(comando_limpeza)
                        print('Opção Inválida.')
                        input('Pressione ENTER para continuar')
            elif opcao == '6':
                break
            else:
                os.system(comando_limpeza)
                print('Opção Inválida.')
                input('Pressione ENTER para continuar')
    elif escolha == '8':
        os.system(comando_limpeza)
        print('Obrigado por usar a Calculadora Python. Até mais!')
        break


            