import math

def omtrek_cirkel(straal):
    if straal < 0:
        return 0
    return 2 * math.pi * straal

def oppervlakte_rechthoek(lengte, breedte):
    if lengte < 0 or breedte < 0:
        return 0
    return lengte * breedte

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

def gemiddelde(getallen):
    if not isinstance(getallen, list):
        return 0
    return sum(getallen) / len(getallen)

if __name__ == "__main__":
   
    print("Omtrek cirkel (straal 3):", omtrek_cirkel(3))            
    print("Omtrek cirkel (negatieve straal):", omtrek_cirkel(-5))   
    print("Oppervlakte rechthoek (5 x 4):", oppervlakte_rechthoek(5, 4))    
    print("Oppervlakte rechthoek (negatieve lengte):", oppervlakte_rechthoek(-2, 3)) 
    print("Pythagoras (3, 4):", pythagoras(3, 4))
    
    print("Gemiddelde van [4, 8, 6]:", gemiddelde([4, 8, 6]))       
    print("Gemiddelde van lege lijst:", gemiddelde([0]))           
    print("Gemiddelde van geen lijst:", gemiddelde("geen lijst"))
    # dit was het
    
