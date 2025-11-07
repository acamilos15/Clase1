def saludar(s):
    print(f"Buenos días {s}")

def par(n):
    return n%2==0

def impar(m):
    return m%2==1 

def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]
