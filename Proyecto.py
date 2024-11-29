#Caculadora de  índice de masa corporal 


nombre=input("Introduzca su nombre:   ")
apellido_materno=input(" Introduzca su apellido materno:  ")
apellido_paterno=input("Introduzca su apellido paterno:  ")
edad=int(input("Introduzca su edad:  "))
peso=float(input("Introduzca su peso en kilogramos:  "))
estatura=float(input("introduzca su estatura en metros: "))
imc = peso / (estatura**2)
print("Su IMC es:", imc)



