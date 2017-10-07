import sys
import time
import types

SIZE_LOG_LINES = 100000;
SIZE_UNIQUE_IPS = 90001;
uniqueIps = [];
#   colecciones
listLogLine = []
dictLogLine = {}
#setLogLine = set()   presenta problemas

def creaLista():
    for i in range(SIZE_LOG_LINES):
        counter = i % SIZE_UNIQUE_IPS
        logLine = [counter, "ip-" + str(counter)]
        listLogLine.append(logLine);

def creaDict():
    for i in range(SIZE_LOG_LINES):
        counter = i % SIZE_UNIQUE_IPS
        ip = "ip-" + str(counter)
        dictLogLine[counter] = ip

def readAllLogs(coleccion,tipo):
    lineas = 0
    if tipo==1:                             # List
        for line in coleccion:
            ip = line[1]  # getIP
            lineas = lineas + 1
    else:                                   # Dict
        for k, v in coleccion.items():
            ip = v        # getIP
            lineas = lineas + 1
    return lineas

def SizeUniqueIps(coleccion,tipo):
    if tipo==1:                             # List
        for line in coleccion:
            ip = line[1]  # getIP
            if not (ip in uniqueIps):
                uniqueIps.add(ip)
    else:                                   # Dict
        for k, v in coleccion.items():
            ip = v  # getIP
            if not (ip in uniqueIps):
                uniqueIps.add(ip)
    return len(uniqueIps);

def ejecutaReadAllLogs(coleccion,tipo):
    ini = time.time()
    res = readAllLogs(coleccion,tipo)
    dt = (time.time() - ini) * 1000  # milisegundos
    print("Number of lines: " + str(res))
    print("Duracion = " + str(dt) + " milisegundos")

def ejecutaSizeUniqueIps(coleccion,tipo):
    ini = time.time()
    res = readAllLogs(coleccion,tipo)
    dt = (time.time() - ini) * 1000  # milisegundos
    print("Number of unique IPs: " + str(res))
    print("Duracion = " + str(dt) + " milisegundos")


def main():
    creaLista()
    creaDict()
    print("1. ReadAllLogs Usando List  ")
    print("2. ReadAllLogs Usando Set   ")
    print("3. SizeUniqueIps Usando List  ")
    print("4. SizeUniqueIps Usando Set   ")
    opc = int(input("    opcion : "))
    if opc==1:
        ejecutaReadAllLogs(listLogLine,1)
    elif opc==2:
        ejecutaReadAllLogs(dictLogLine,2)
    elif opc==3:
        ejecutaSizeUniqueIps(listLogLine,1)
    elif opc==4:
        ejecutaSizeUniqueIps(dictLogLine,2)

# programa principal
main()
