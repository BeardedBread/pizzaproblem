import numpy as np

def slice_pizza():
    pass

f = open('small.in','r')

info = []
for line in f:
    info.append(line.strip('\n'))
f.close()
#print(info)

pizza_dim = info[0].split(' ')
print(pizza_dim)
n_T = 0;n_M =0;
pizza = np.zeros([int(pizza_dim[0]),int(pizza_dim[1])],dtype = str)
for i in range(int(pizza_dim[0])):
    for j in range(int(pizza_dim[1])):
        pizza[i][j] = info[i+1][j]
        if info[i+1][j] == 'T':
            n_T +=1
        else:
            n_M +=1

print(pizza)
print('T:',n_T,'M:',n_M)

if n_T > n_M:
    ing_sel = 'M'
else:
    ing_sel = 'T'
#f = open('pizza_sol,txt','w')
for i in range(pizza_dim[0]):
    for j in range(pizza_dim[1]):
        if pizza[i][j] == ing_sel:
            pizza,n_slices = slice_pizza(pizza,n_slices)







#f.close()
