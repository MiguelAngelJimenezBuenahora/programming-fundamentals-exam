#4. Desarrolle el código fuente de un programa que permita ingresar y leer el valor correspondiente a una distancia en metros y la visualice expresadas en km.
#
#   Para convertir `metros` a `kilómetros`, puedes usar la siguiente fórmula: KM = m/1000
meters = float(input(""""In this program , you enter yous length on metters and i'll convert that length to km 
Please enter the length you want to convert: """))
print(f"""The length on km is {round((meters/1000),2)}""")