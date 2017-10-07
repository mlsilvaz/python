import sys
import time

fibonacciCache = []

# Complexity: O(2 ^ N)
def fibonacci1(n):
    try:
        if n < 0:
            raise ZeroDivisionError
        if (n <= 2):
            return 1
        return fibonacci1(n - 1) + fibonacci1(n - 2);
    except ZeroDivisionError:
        print("N can not be less than zero")
    except :
        print("Error inesperado:", sys.exc_info()[0])
# Complexity: O(N)
def fibonacci2(n):
    try:
        if n < 0:
            raise ZeroDivisionError
        if (n <= 2):
            return 1
        fibonacci = 0;
        previous = 1;
        penultimo = 0;
        for i in range(1, n+1):
             penultimo = fibonacci
             fibonacci = previous + fibonacci
             previous = penultimo
        return fibonacci;
    except ZeroDivisionError:
        print("N can not be less than zero")
    except :
        print("Error inesperado:", sys.exc_info()[0])
# Complexity: O(N)
def fibonacci3(n):
    try:
        if n < 0:
            raise ZeroDivisionError
        if (n <= 2):
            fibonacciCache[n] = 1
        if (fibonacciCache[n] == 0):
            fibonacciCache[n] = fibonacci3(n - 1) + fibonacci3(n - 2);
        return fibonacciCache[n];
    except ZeroDivisionError:
        print("N can not be less than zero")
    except:
        print("Error inesperado:", sys.exc_info()[0])

def ejecutaFibonacci1(n):
    ini = time.time()
    res = fibonacci1(n)
    dt = (time.time() - ini) * 1000  # milisegundos
    print("O(2^N) N=" + str(n) + " -> " + str(res))
    print("Duracion = " + str(dt) + " milisegundos")

def ejecutaFibonacci2(n):
    ini = time.time()
    res = fibonacci2(n)
    dt = (time.time() - ini) * 1000  # milisegundos
    print("O(N) N=" + str(n) + " -> " + str(res))
    print("Duracion = " + str(dt) + " milisegundos")

def ejecutaFibonacci3(n):
    #
    for i in range(n+1):
        fibonacciCache.append(0)
    ini = time.time()
    res = fibonacci3(n)
    dt = (time.time() - ini) * 1000  # milisegundos
    print("O(N) N=" + str(n) + " -> " + str(res))
    print("Duracion = " + str(dt) + " milisegundos")

#programa principal
n = 20
#ejecutaFibonacci1(n)
ejecutaFibonacci2(n)
#ejecutaFibonacci3(n)

