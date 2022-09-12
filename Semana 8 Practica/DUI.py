#INTEGRANTE: Jonathan Elias Gamez Larin

def dui():

     DUI_I = input("Digite Su DUI: ")

     if DUI_I.isdigit():
        
        if len(DUI_I) == 9:
            return("DUI VALIDO")

        else:
            return("DUI INVALIDO")


