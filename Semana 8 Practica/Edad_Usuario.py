#INTEGRANTE: Jonathan Elias Gamez Larin

def age():
    while True:
        try:
           ages = int(input("Digite su año de nacimiento: "))

        except ValueError:
            print("Fecha Invalida...")
            continue

        ages_y = 2022 - ages
        if ages_y >= 18:
            print("Eres mayor de edad...")
            break
        
        elif ages_y >= 0:
            print("Eres menor de edad...")
            break
            
        elif ages_y < 0:
            print("Fecha Invalida...")
            break
            
 
    

