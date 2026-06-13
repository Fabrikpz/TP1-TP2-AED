tratamientos = open("tratamientos.txt", "rt")

def lineaAdicional(linea):
    montoAL = int(linea[2:8])
    montoMZ = int(linea[8:14])
    montoU = int(linea[14:20])
    
    return montoAL, montoMZ, montoU

def leer_lineas():
    for linea in tratamientos:
        if linea[0] == "#":
            m_AL, m_MZ, m_U = lineaAdicional(linea)
        else:
            r1+=1
            
        

leer_lineas() # 296645 352478 207261
tratamientos.close()