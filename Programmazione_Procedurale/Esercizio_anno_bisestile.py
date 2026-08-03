# I criteri per determinare se un anno è bisestile sono i seguenti:
# 1. Un anno è bisestile se è divisibile per 4
# 2. Tuttavia, se l'anno è divisibile per 100, non è bisestile
# 3. Ma se l'anno è divisibile per 400, allora è bisestile

def is_bisestile(anno):
    bisestile = False
    if anno%4 == 0:
        if anno%100 == 0:
            if anno%400 == 0:
                bisestile = True
        else: 
            bisestile = True
    return bisestile
    
anno = int(input("Inserisci un anno: "))

if is_bisestile(anno) == True:
    print(f"L'anno {anno} è bisestile.")
else:
    print(f"L'anno {anno} non è bisestile.")