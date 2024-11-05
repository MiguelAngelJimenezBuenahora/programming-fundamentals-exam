#Desarrolle un programa que solicite ingrese tres voltajes distintos e indique si el promedio de los voltajes ingresados es menor a 115 visualice
# `"VOLTAJE CORRECTO"`, caso contrario sea mayor a 115 y menor a 220 visualice `"ALTO VOLTAJE"`, y si es mayor a 220 visualice `"PELIGRO"`.

Voltage1 =int(input("""In this program i'l calculate the average voltage and say you if the voltage is the correct voltage, high voltage or danger
Please enter the first voltage: """)) 
Voltage2 =int(input("Please enter the second voltage: "))
Voltage3 =int(input("Please enter the third voltage: "))
average = ((Voltage1 + Voltage2 + Voltage3)/3)
if average >=220:
    Print("Danger")
    elif average >=115 and average<220:
        Print("High voltage")
    else:
        Print("Correct voltage")
