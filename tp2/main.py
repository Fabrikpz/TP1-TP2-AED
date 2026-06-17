tratamientos = open("tratamientos.txt", "rt")

def lineaAdicional(linea):
    montoAL = int(linea[2:8])
    montoMZ = int(linea[8:14])
    montoU = int(linea[14:20])
    
    return montoAL, montoMZ, montoU

def limpiar_espacios(cadena):
    pos = len(cadena)
    while pos > 0 and cadena[pos - 1] == " ":
        pos -= 1
    return cadena[:pos]

def monto_final(linea, m_AL, m_MZ, m_U):
    monto_base = int(linea[31:39])
    
    if "A" <= linea[25] <= "L":
        monto_adicional = m_AL
    elif "M" <= linea[25] <= "Z" and linea[25] != "U":
        monto_adicional = m_MZ
    else: 
        monto_adicional = m_U
    
    codigo = linea[25:31]
    porcentaje = int(codigo[4:])
    
    base_completa = monto_base + monto_adicional
    subtotal = base_completa + (base_completa * porcentaje / 100)
    
    if len(linea) >= 40 and linea[39] == "X":
        subtotal = subtotal * 1.05
    
    return subtotal

def leer_lineas():
    r1 = r2 = r3 = r4 = r5 = r6 = cant_cap19 = suma_monto_cap19 = r7 = r9 = cant_alta_comp = sum_total_montos = 0
    m_AL = m_MZ = m_U = 0
    r8 = ""
    for linea in tratamientos:
        if linea[0] == "#":
            m_AL, m_MZ, m_U = lineaAdicional(linea)
        else:
            r1 += 1
            
            nombre_limpio = limpiar_espacios(linea[0:25])
            codigo_limpio = limpiar_espacios(linea[25:31])
            m_final = monto_final(linea, m_AL, m_MZ, m_U)
            
            sum_total_montos += m_final
            
            if linea[25] == "A":
                r2 += 1
            if linea[25] == "B":
                r3 += 1
            if linea[25] == "C":
                r4 += 1
            if linea[25] == "E":
                r5 += 1
            if linea[25] == "P":
                r6 += 1
            if linea[25] == "S" or linea[25] == "T":
                cant_cap19 += 1
                suma_monto_cap19 += m_final
            if linea[25] != "U":
                if m_final > r9:
                    r9 = m_final
                    r8 = nombre_limpio
            if len(linea) >= 40 and linea[39] == "X":
                cant_alta_comp += 1
                
    prom_total_pagado = sum_total_montos / r1
    
    archivo_segunda_pasada = open("tratamientos.txt", "rt")
    
    m_AL_2 = m_MZ_2 = m_U_2 = 0
    alta_que_superan_promedio = 0
    
    for linea in archivo_segunda_pasada:
        if linea[0] == "#":
            m_AL_2, m_MZ_2, m_U_2 = lineaAdicional(linea)
        else:
            m_final = monto_final(linea, m_AL_2, m_MZ_2, m_U_2)
            es_alta = len(linea) >= 40 and linea[39] == "X"

            if es_alta and m_final > prom_total_pagado:
                alta_que_superan_promedio += 1
                
    archivo_segunda_pasada.close()
                
    r7 = round(suma_monto_cap19 / cant_cap19, 2)   
    r9 = round(r9, 2)
    r10 = int(alta_que_superan_promedio * 100 / cant_alta_comp) 
    tratamientos.close()
    print('(r1) - Cantidad de tratamientos cargados:', r1) 
    print('(r2) - Cantidad de tratamientos "A":', r2) 
    print('(r3) - Cantidad de tratamientos "B":', r3) 
    print('(r4) - Cantidad de tratamientos "C":', r4) 
    print('(r5) - Cantidad de tratamientos "E":', r5) 
    print('(r6) - Cantidad de tratamientos "P":', r6) 
    print('(r7) – Importe final promedio (capítulo 19):', r7) 
    print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final:', r8) 
    print('(r9) - Mayor importe pagado por ese paciente):', r9) 
    print('(r10)- Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:', r10)

leer_lineas()