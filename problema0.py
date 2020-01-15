num = ["uno", "dos", "tres", "cuatro", "cinco",
       "seis", "siete", "ocho", "nueve", "diez"]
num2 = ["once", "doce", "trece", "catorce", "quince",
        "dieciseis", "diescisiete", "diesciocho", "diescinueve"]
num20 = ["veinte"]
num30 = ["treinta"]
num40 = ["cuarenta"]
num50 = ["cincuenta"]
num60 = ["secenta"]
num70 = ["setenta"]
num80 = ["ochenta"]
num90 = ["noventa"]

x = int(input("Ingrese un numero porfavor: "))

if (x <= 10):
    print(num[x - 1])
elif (x <= 19):
    print(num2[x - 11])
elif (x == 20):
    print(num20[0])
elif (x > 20 and x < 30):
    print(num20[0] + " y " + num[x - 21])
elif (x == 30):
    print(num30[0])
elif (x > 30 and x < 40):
    print(num30[0] + " y " + num[x - 31])
elif (x == 40):
    print(num40[0])
elif (x > 40 and x < 50):
    print(num40[0] + " y " + num[x - 41])
elif (x == 50):
    print(num50[0])
elif (x > 50 and x < 60):
    print(num50[0] + " y " + num[x - 51])
elif (x == 60):
    print(num60[0])
elif (x > 60 and x < 70):
    print(num60[0] + " y " + num[x - 61])
elif (x == 70):
    print(num70[0])
elif (x > 70 and x < 80):
    print(num70[0] + " y " + num[x - 71])
elif (x == 80):
    print(num80[0])
elif (x > 80 and x < 90):
    print(num80[0] + " y " + num[x - 81])
elif (x == 90):
    print(num90[0])
elif (x > 90 and x < 1000):
    print(num90[0] + " y " + num[x - 91])
elif (x == 1000):
    print("mil")
else:
    print("Numero muy alto.")
