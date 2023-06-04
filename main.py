from hermite import hermite, hermitePolynomial,getPolynomial



def main():
    while True:

        ifun = int(input("Wybierz funkcje:(1. x^3+3x^2+2x+1, 2. cos(2x), 3. 2sin(x), 4. |x|, 5. 2x+3, 6. Koniec): "))
        if ifun < 1 or ifun > 5:
            return
        degree = int(input("Podaj stopień wielomianiu:"))
        print("Na ilu węzłach ma być obliczona całka?[2,3,4,5]")
        nod = int(input())
        getPolynomial(ifun,nod,degree)






if __name__ == '__main__':
    main()