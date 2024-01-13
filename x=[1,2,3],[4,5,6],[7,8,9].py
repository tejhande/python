x=[1,2,3],[4,5,6],[7,8,9]
y=[1,2,3,4],[8,14,12,21],[11,3,6,8]
result=[0,0,0,0],[0,0,0,0],[0,0,0,0]

for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(y)):
            result[i][j]=x[i][k]*y[k][j]
print(result)
