#item a
elementos = 4
elemento = 1
while(elementos > 0):
    elemento += 2
    elementos -= 1

print(elemento) #resposta 9

#item b
elementos = 6
elemento = 2
while(elementos > 0):
    elemento *= 2
    elementos -= 1

print(elemento) #resposta 128

#item c
elementos = 7
elemento = 0
a_somar = 1
while(elementos > 0):
    elemento += a_somar
    a_somar += 2        
    elementos -= 1

print(elemento) #resposta 49

#item d
elementos = 4
elemento = 4
impar = 3

while(elementos > 0):
    a_somar = (impar*4)
    elemento += a_somar
    impar += 2
    elementos -= 1

print(elemento) #resposta 100

#item e

fibonacci = [1,1,2]
for i in range (2, 6):
    fibonacci.append(fibonacci[i]+fibonacci[i-1])
    print(fibonacci) #reposta 13
'''
#item f
elementos = 4
elemento = 1
while(elementos > 0):
    elemento += 2
    elementos -= 1

print(elemento) #resposta 9
'''