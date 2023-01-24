import os 

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
        
#Declaracion de los metodos de la clase 
def main(): 
    os.system('cls')
    obj=OpearacionesBas(3,4)
    obj.suma()

if __name__ == "__main__":
    main()




    #Declaracion de propiedades de clase 