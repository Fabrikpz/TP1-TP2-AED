beneficiario = input()
codigo = input()
monto_base = int(input())

monto_final = monto_base + 25000

letra = codigo[0]

if "A" <= letra <= "L":
    monto_final += 25000
elif letra == "U":
    monto_final += 100000
elif "M" <= letra <= "Z" and letra != "U":
    monto_final += 40000

if len(codigo) > 5:
    porcentaje = int(codigo[4] + codigo[5])
else:
    porcentaje = int(codigo[4])

monto_final += (monto_final * porcentaje) // 100

texto_bloque = codigo[1] + codigo[2]
bloque = int(texto_bloque)

if letra == "A" or letra == "B":
    capitulo = "Ciertas enfermedades infecciosas y parasitarias"
elif letra == "C":
    capitulo = "Tumores [neoplasias]"
elif letra == "D":
    if bloque <= 48:
        capitulo = "Tumores [neoplasias]"
    else:
        capitulo = "Enfermedades de la sangre y de los órganos hematopoyéticos y ciertos trastornos que afectan el mecanismo de la inmunidad"
elif letra == "E":
    capitulo = "Enfermedades endocrinas, nutricionales y metabólicas"
elif letra == "F":
    capitulo = "Trastornos mentales y del comportamiento"
elif letra == "G":
    capitulo = "Enfermedades del sistema nervioso"
elif letra == "H":
    if bloque <= 59:
        capitulo = "Enfermedades del ojo y sus anexos"
    else:
        capitulo = "Enfermedades del oído y de la apófisis mastoides"
elif letra == "I":
    capitulo = "Enfermedades del sistema circulatorio"
elif letra == "J":
    capitulo = "Enfermedades del sistema respiratorio"
elif letra == "K":
    capitulo = "Enfermedades del sistema digestivo"
elif letra == "L":
    capitulo = "Enfermedades de la piel y del tejido subcutáneo"
elif letra == "M":
    capitulo = "Enfermedades del sistema osteomuscular y del tejido conjuntivo"
elif letra == "N":
    capitulo = "Enfermedades del sistema genitourinario"
elif letra == "O":
    capitulo = "Embarazo, parto y puerperio"
elif letra == "P":
    capitulo = "Ciertas afecciones originadas en el período perinatal"
elif letra == "Q":
    capitulo = "Malformaciones congénitas, deformidades y anomalías cromosómicas"
elif letra == "R":
    capitulo = "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"
elif letra == "S" or letra == "T":
    capitulo = "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"
elif "V" <= letra <= "Y":
    capitulo = "Causas externas de morbilidad y mortalidad"
elif letra == "Z":
    capitulo = "Factores que influyen en el estado de salud y contacto con los servicios de salud"
elif letra == "U":
    capitulo = "Códigos para propósitos especiales"
else:
    capitulo = "Capítulo Desconocido"

print("Beneficiario:", beneficiario)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", monto_final)