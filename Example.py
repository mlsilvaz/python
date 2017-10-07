import sys

N = 8;					            # para la opcion 1,2,3
def getValueList():		            # para la opcion 4,5
    return [2, 4, 4, 5, 7, 10, 23, 25, 64]

    #	Complexity: O(N)
def loop(N):
    try:
        counter = 0;
        while counter < N:
            print(counter)
            counter = counter + 1
    except:
        print("Error inesperado:", sys.exc_info()[0])

# Complexity: O(N*N)
def createAllPairs(N):
    try:
        x = 0;
        y = 0;
        while x < N:
            y = 0
            while y < N :
                print(x, y)
                y = y + 1
            x = x + 1
    except:
        print("Error inesperado:", sys.exc_info()[0])

# Complexity: O(N)
def factorial(N):
    try:
        if N == 1:
            return 1
        return N * factorial(N - 1)
    except:
        print("Error inesperado:", sys.exc_info()[0])

# Complexity: O(N)
def containsNeedle(needle, valueList):
    try:
        for value in valueList:
            if value == needle:
                return True
        return False

    except:
        print("Error inesperado:", sys.exc_info()[0])


# Complexity: O(log2 N)
def binarySearch(valueList, needle, min, max):
    try:
        midpoint = (max + min) // 2
        if (len(valueList) > 0) and (valueList[midpoint] == needle):
            return midpoint
        if min >= max:
            return -1
        if valueList[midpoint] > needle:
            return binarySearch(valueList, needle, min, midpoint - 1)
        return binarySearch(valueList, needle, midpoint + 1, max)
    except:
        print("Error inesperado:", sys.exc_info()[0])

def main():
    valueList = getValueList()
    print("1. Loop           ")
    print("2. CreateAllPairs ")
    print("3. Factorial      ")
    print("4. ContainsNeedle ")
    print("5. BinarySearch   ")
    opc = int(input("     opcion : "))
    if opc==1:
        loop(N)
    elif opc==2:
        createAllPairs(N)
    elif opc==3:
        fact = factorial(N)
        print("Factorial " + str(N) + " = " + str(fact))
    elif opc==4:
        buscar = 25
        found = containsNeedle(buscar, valueList)
        print("Number " + str(buscar) + " was found ")
    elif opc==5:
        buscar = 64
        position = binarySearch(valueList, buscar, 0, len(valueList)-1)
        if position == -1:
            print("not found")
        else:
            print("Number " + str(buscar) + " found at position : " + str(position))

# programa principal
main()
