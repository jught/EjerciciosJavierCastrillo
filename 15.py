#15 Pedir una frase y un número “N” y devolver la frase repetida N veces
try : 
    x = str(input("Dime algo, una frase \n - "))+" || "
    N = int(input("Dame un numero, por favor \n  N = "))
except : 
    print("Algo me has metido mal ya, majo")
print("||", (N*x)[:-1])
