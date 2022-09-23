from cmath import sqrt
from collections import namedtuple

V3 = namedtuple('Point3', ['x', 'y', 'z'])

def matrix_multiplication(X,Y):
    result = []

    for i in range(len(X)):
        row = []
        for j in range(len(Y[0])):
            row.append(0)

        for j in range(len(Y[0])):
            for k in range(len(Y)):
                row[j] += ((X[i][k] * Y[k][j]).real)
        
        result.append(row)
    
    return result

def vector_matrix_multiplication(X, V):
    result = []
    for i in range(len(X)):
        total = 0
        for j in range(len(V)):
            total += ((V[j] * X[i][j]).real)
        result.append(total)
    return result

def cross(X,Y):
    x = X.y*Y.z - Y.y*X.z
    y = X.z*Y.x - Y.z*X.x
    z = X.x*Y.y - Y.x*X.y
    return V3((x.real),(y.real),(z.real))

def subtract(X,Y):
    x=X.x-Y.x
    y=X.y-Y.y
    z=X.z-Y.z
    return V3((x.real),(y.real),(z.real))

def normalized (X):
    try:
        m = sqrt( X.x**2 + X.y**2 + X.z**2 )
        x = X.x / m
        y = X.y / m
        z = X.z / m
        #print(sqrt( X.x**2 + X.y**2 + X.z**2 ), x, y, z)
        return V3((x.real),(y.real),(z.real))
    except:
        return

def magnitude(X):
    try:
        return sqrt( X.x**2 + X.y**2 + X.z**2 ).real
    except:
        return

def dot(X,Y):
    r = X[0]*Y[0] + X[1]*Y[1] + X[2]*Y[2]
    return (r.real)

def toggleSign(X):
    return V3(-1*X.x,-1*X.y, -1*X.z)

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    #pr(m)
    determinant = getMatrixDeternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = list(transposeMatrix(cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def escalarVectorMultiplication(e,v):
    return V3(v[0]*e,v[1]*e,v[2]*e)

def vectorAddition(X,Y):
    return V3(X[0]+Y[0], X[1]+Y[1],X[2]+Y[2])