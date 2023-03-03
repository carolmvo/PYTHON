number = int(input("Digite um número: "))

def par_impar(number):
    if number % 2 == 0:
        parouimpar = "par"
    else:
        parouimpar = "impar"
    return parouimpar

print(f"Seu número é {par_impar(number)}!")
