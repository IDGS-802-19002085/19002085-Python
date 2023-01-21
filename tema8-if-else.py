print("suma de nuemros")
num1=int(input('dame num 1;'))
num2=int(input('dame num 2;'))


if num1 > num2 :
    print("el {} es mayor que el {}".format(num1,num2))
else :
    print("el {} es mayor que el {}".format(num1,num2))

print("--------------Pedir una edad-------------")
edad= int(input('Ingresa tu edad: '))


if edad > 18: 
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años ")
else: 
    print("No esres mayor de edad")
