#import os 

class OpearacionesBas: 
    #Deckaracion de propiedades 
    #num1=0
    # num2=0
    res=0


    #Declaracion del constructor 
    def __init__(self, a,b):
        self.num1=a
        self.num2=b 

    def suma(self):
        #num1=12

        #num2=10
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))

    def resta(self):
        #num1=12
        #num2=10
        self.res=self.num1-self.num2
        print("La resta es: {}".format(self.res))

    def multi(self):
        #num1=12
        #num2=10
        self.res=self.num1*self.num2
        print("La multi es: {}".format(self.res))


    def divi(self):
        #num1=12
        #num2=10
        self.res=self.num1/self.num2
        print("La divi es: {}".format(self.res))
        
#Declaracion de los metodos de la clase 


def main(): 
    opcion=-1
    while (opcion != 5):
        opcion=int(input("1- Suma. 2-Resta- 3-Multiplicacion 4-Division 5-Salir"))
        if (opcion == 5):
            break
        num1=int(input('Ingresa el primer valor '))
        num2=int(input('Ingresa el segundo valor'))
        if(opcion ==1 ):
                    obj=OpearacionesBas(num1,num2)
                    obj.suma()
        if(opcion ==2): 
                    obj=OpearacionesBas(num1,num2)
                    obj.resta
        if(opcion ==3): 
                    obj=OpearacionesBas(num1,num2)
                    obj.multi

        if(opcion ==4): 
                    obj=OpearacionesBas(num1,num2)
                    obj.divi
        print("La resta es: {}".format(self.res))

        

if __name__ == "__main__":
    main()




    #Declaracion de propiedades de clase 