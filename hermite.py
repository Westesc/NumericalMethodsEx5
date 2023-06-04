from functions import funtionsAll, power

nodes = [[-0.707107, 0.707107], [-1.22475, 0, 1.22475], [-1.65068, -0.524648, 0.524648, 1.65068],
         [-2.02018, -0.958573, 0, 0.958573, 2.02018]]

weights = [[0.886227, 0.886227], [0.295409, 1.181636, 0.295409], [0.081313, 0.804914, 0.804914, 0.081313],
           [0.019953, 0.393619, 0.945309, 0.393619, 0.019953]]

ar = [[0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 2, 0],
      [0, 0, 0, 0, 0, 4, 0, -2],
      [0, 0, 0, 0, 8, 0, -12, 0],
      [0, 0, 0, 16, 0, -48, 0, 12],
      [0, 0, 32, 0, -160, 0, 120, 0],
      [0, 64, 0, -480, 0, 720, 0, -120],
      [128, 0, -1344, 0, 3360, 0, -1680, 0]]


def hermite(ifun, n):
    ret = 0
    for i in range(0, n):
        ret += weights[n - 2][i] * funtionsAll(nodes[n - 2][i], ifun)
    return ret

def calA(ifun, n,number):
    ret = 0
    for i in range(0, n):
        ret += weights[n - 2][i] * funtionsAll(nodes[n - 2][i], ifun) * hermitePolynomial(number,nodes[n-2][i])
    return ret

def hermitePolynomial(i,x):
    j = 0
    result = 0
    while j < 8:
        if ar[i][j] != 0:
            result += ar[i][j]*power(j,x)
        j += 1
    return result

def getPolynomial(ifun,n,degree):
    i = 0
    s = []
    while i <= degree:
        a =calA(ifun,n,i)
        j = 0
        t =0
        print("a:")
        print(a)
        while j < 7:
            if ar[i][j] != 0:
                t += (ar[i][j] * a)
            j+=1
        s.append(t)
        print("t:")
        print(t)
        i+=1





