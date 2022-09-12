#INTEGRANTE: Jonathan Elias Gamez Larin

import Edad_Usuario
import DUI

Start = int(input("Ingrese -1- para calcular su edad o Ingrese -2- para su DUI: "))
if Start == 1:
    age_C = Edad_Usuario.age()
    print(age_C)

elif Start == 2:
    DUI_C = DUI.dui()
    print(DUI_C)

else:
    print("No existe esa opcion...")
    

