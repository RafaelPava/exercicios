def verifica_fibonacci(numero):
    fibonacci = [0,1,1]
    if numero == 0 or numero == 1:
        print(fibonacci)
        print(f"O número passado ({numero}) pertence à sequência de Fibonacci")
        return
    for i in range (2, numero + 1):
        fibonacci.append(fibonacci[i]+fibonacci[i-1])
        if fibonacci[i] == numero:
            print(fibonacci)
            print(f"O número passado ({numero}) pertence à sequência de Fibonacci")
            return

numero = int(input('Qual número deseja verificar se está na sequência de Fibonacci?\n'))
verifica_fibonacci(numero)