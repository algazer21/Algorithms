# Uses python3
#Ya sé, puede ser bastante más bonito, pero funciona muy bien.

def edit_distance(s, t):
    s, t = ' ' + s, ' ' + t
    m,n = len(s), len(t)
    ara = []

    for i in range(m):                      #Crear primera fila de matriz
        ara.append(i)
        
    for i in range(1,n):
        arb = [i]*m                         #Creo arreglo auxiliar
        for j in range(1,m):                 
            mi = ara[j-1]                   #Esto es para encontrar el mínimo
            
            if ara[j] < mi:
                mi = ara[j]
                
            if arb[j-1] < mi:
                mi = arb[j-1]
                           
            if s[j] == t[i]:                #Esto es para calcular distancia
                arb[j] = ara[j-1]
                
            elif s[j] != t[i]:
                arb[j] = mi+1
        ara = arb
     
    return ara[m-1]

if __name__ == "__main__":
    #print(edit_distance(input(), input()))
    print(edit_distance('short', 'ports'))
