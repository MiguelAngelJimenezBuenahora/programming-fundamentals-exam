#Eexercise 1
Voltage1 =float(input("""In this program i'll request to you insert the '5 Voltage's' and i'll saw you the average, and say you if is 'High voltage'}
Please enter the first voltage: """))
Voltage2 =float(input("Please enter the second voltage: "))
Voltage3 =float(input("Please enter the third voltage: "))
Voltage4 =float(input("Please enter the fourth voltage: "))
Voltage5 =float(input("Please enter the fifth voltage: "))
Average = ((Voltage1+Voltage2+Voltage3+Voltage4+Voltage5)/5)
if average >=220:
    print("High voltage")
    else:
        print("Correct voltage")