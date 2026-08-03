# I criteri per determinare se un anno è bisestile sono i seguenti:
# 1. Un anno è bisestile se è divisibile per 4
# 2. Tuttavia, se l'anno è divisibile per 100, non è bisestile
# 3. Ma se l'anno è divisibile per 400, allora è bisestile

def is_bisestile(anno):
    if anno%4 != 0 :
        print(f"{anno} non è bisestile")
    else:
        if anno%100 == 0:
            if anno%400 != 0:
                print(f"{anno} non è bisestile")
            else: 
                print(f"{anno} è bisestile")
        
        else: print(f"{anno} è bisestile")
    
anno = int(input("Inserisci un anno: "))

is_bisestile(anno)