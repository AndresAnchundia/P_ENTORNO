def sum(num1, num2):
    suma = num1 + num2 
    return suma

def resta(num1, num2):
    resta = num1 - num2
    return resta

def multiplicacion(num1, num2):
    multi = num1 * num2
    return multi

def division(num1, num2):
    div = num1 / num2
    return div



print ("---------------Calculadora Basica-------------")

num1 = int(input("ingrese el primer numero ->"))
num2 = int(input("ingres el segundo numero ->"))



print ("escoja la opcion a calcualar ->")

while True: 
    print("sumar == 1 ")
    print("restar == 2 ")
    print("multiplicar == 3 ")
    print("dividir == 4 ")
    print("salir == 5")
    opcion = int(input("Ingreseel numero a la opcion a realizar "))
    if opcion == 1:
        print("      ")
        print("la suma es ->",sum(num1,num2))
        print("      ")
        pass
    elif opcion == 2:
        print("      ")
        print("la resta es ->",resta(num1,num2))
        print("      ")
    elif opcion == 3:
        print("      ")
        print("la multiplicacion es ->",multiplicacion(num1,num2))
        print("      ")
    elif opcion == 4:
        print("      ")
        print("la division es ->",division(num1,num2))
        print("      ")
    elif opcion == 5:
        break
    else:
        print("")
        print("valor incorrecto!!!!!!!!!!!!!!!!!!!!")
        print("")
        
#fin del código.        

        print("")
        print("valor incorrecto!!!!!!!!!!!!!!!!!!!!")
        print("")