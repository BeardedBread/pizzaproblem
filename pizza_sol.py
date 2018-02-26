import numpy as np
import math

def slice_pizza(i,j,pizza,n_slices,pizza_dim):
    sliced = False
    possible_slice=np.array([])
    leftbound=j
    upperbound=i
    rightbound=j
    lowerbound=i
    expand=0 #number of times the check area expand
    while sliced==False and (expand+1)<pizza_dim[3]:
        #expand square and check if fulfill L
        if leftbound!=0:
            leftbound-=1
        if upperbound!=0:
            upperbound-=1
        if rightbound!=pizza_dim[1]-1:
            rightbound+=1
        if lowerbound!=pizza_dim[0]-1:
            lowerbound+=1
        expand+=1
        fulfilled=check_pizza([upperbound,leftbound],[lowerbound,rightbound],pizza,pizza_dim[2])
        if fulfilled:
            for n in range(upperbound+1,i+1):
                for m in range(leftbound+1,j+1):
                    for r in range(i,lowerbound+1):
                        c=rightbound
                        below_maxsize,size=check_size([upperbound,leftbound],[lowerbound,rightbound],pizza_dim[3])
                        if below_maxsize: #skip check if the slice is bigger than H
                            if possible_slice.size==0:
                                if check_pizza([n,m],[r,c],pizza,pizza_dim[2]): # check for enough no of T & M
                                    if ~np.any(pizza[n:r,m:c]=='-'): #check shape
                                          possible_slice=np.array([[n,m,r,c,size]])
                            elif size<min(possible_slice[:,4]):
                                if check_pizza([n,m],[r,c],pizza,pizza_dim[2]): # check for enough no of T & M
                                    if ~np.any(pizza[n:r,m:c]=='-'): #check shape
                                        possible_slice=np.append(possible_slice,[[n,m,r,c,size]],0)
                    for c in range(j,rightbound):
                        r=lowerbound
                        below_maxsize,size=check_size([upperbound,leftbound],[lowerbound,rightbound],pizza_dim[3])
                        if below_maxsize: #skip check if the slice is bigger than H
                            if possible_slice.size==0:
                                if check_pizza([n,m],[r,c],pizza,pizza_dim[2]): # check for enough no of T & M
                                    if ~np.any(pizza[n:r,m:c]=='-'): #check shape
                                          possible_slice=np.array([[n,m,r,c,size]])
                            elif size<min(possible_slice[:,4]):
                                if check_pizza([n,m],[r,c],pizza,pizza_dim[2]): # check for enough no of T & M
                                    if ~np.any(pizza[n:r,m:c]=='-'): #check shape
                                        possible_slice=np.append(possible_slice,[[n,m,r,c,size]],0)
            for n in range(upperbound,i+1):
                m=leftbound
                for r in range(i,lowerbound+1):
                    for c in range(j,rightbound+1):
                        below_maxsize,size=check_size([upperbound,leftbound],[lowerbound,rightbound],pizza_dim[3])
                        if below_maxsize: #skip check if the slice is bigger than H
                            if possible_slice.size==0:
                                if check_pizza([n,m],[r,c],pizza,pizza_dim[2]): # check for enough no of T & M
                                    if ~np.any(pizza[n:r,m:c]=='-'): #check shape
                                          possible_slice=np.array([[n,m,r,c,size]])
                            elif size<min(possible_slice[:,4]):
                                if check_pizza([n,m],[r,c],pizza,pizza_dim[2]): # check for enough no of T & M
                                    if ~np.any(pizza[n:r,m:c]=='-'): #check shape
                                        possible_slice=np.append(possible_slice,[[n,m,r,c,size]],0)
            for m in range(leftbound+1,j+1):
                n=upperbound
                for r in range(i,lowerbound+1):
                    for c in range(j,rightbound+1):
                        below_maxsize,size=check_size([upperbound,leftbound],[lowerbound,rightbound],pizza_dim[3])
                        if below_maxsize: #skip check if the slice is bigger than H
                            if possible_slice.size==0:
                                if check_pizza([n,m],[r,c],pizza,pizza_dim[2]): # check for enough no of T & M
                                    if ~np.any(pizza[n:r,m:c]=='-'): #check shape
                                          possible_slice=np.array([[n,m,r,c,size]])
                            elif size<min(possible_slice[:,4]):
                                if check_pizza([n,m],[r,c],pizza,pizza_dim[2]): # check for enough no of T & M
                                    if ~np.any(pizza[n:r,m:c]=='-'): #check shape
                                        possible_slice=np.append(possible_slice,[[n,m,r,c,size]],0)
            if possible_slice.size!=0:
                possible_slice= possible_slice[possible_slice[:,4].argsort()][0]#take smallest slice
                sliced=True
                #remove slice from pizza
                for pr in range(possible_slice[0],possible_slice[2]+1):
                    for pc in range(possible_slice[1],possible_slice[3]+1):
                        pizza[pr][pc]='-'
                #print(pizza)
                n_slices+=1
    if not sliced:
        #print(pizza[upperbound:lowerbound,leftbound:rightbound])
        print(i,j,'not sliced')
    else:
        #print('expand:',expand)
        print(i,j,'sliced',possible_slice)
    return pizza,n_slices, possible_slice[0:4]

def check_size(topleft,bottomright,H):
    size=(bottomright[0]-topleft[0])*(bottomright[1]-topleft[1])
    if size>H:
        return False, size
    else:
        return True,size

def check_pizza(topleft,bottomright,pizza,L):
    n_T=0
    n_M=0
    for i in range(topleft[0],bottomright[0]+1):
        for j in range(topleft[1],bottomright[1]+1):
            if pizza[i][j] == 'T':
                n_T +=1
            else:
                n_M +=1
    if n_T>=L and n_M>=L:
        return True
    else:
        return False

f = open('small.in','r')

info = []
for line in f:
    info.append(line.strip('\n'))
f.close()
#print(info)

pizza_dim = info[0].split(' ')
pizza_dim = [int(p) for p in pizza_dim]
print(pizza_dim)
n_T = 0;n_M =0;
pizza = np.zeros([pizza_dim[0],pizza_dim[1]],dtype = str)
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
    max_slices=math.floor(n_M/pizza_dim[2])
else:
    ing_sel = 'T'
    max_slices=math.floor(n_T/pizza_dim[2])
n_slices=0;pizza_slices = []
for i in range(pizza_dim[0]):
    for j in range(pizza_dim[1]):
        if pizza[i][j] == ing_sel:
            pizza,n_slices,pizza_slice = slice_pizza(i,j,pizza,n_slices,pizza_dim)
            pizza_slices.append(pizza_slice)

print('max no of slices:',max_slices)
print('no of slices:',n_slices)


f = open('pizza_sol.txt','w')
f.write(str(n_slices)+'\n')
[f.write(str(ps).strip('[]')+'\n') for ps in pizza_slices if ps.size]
f.close()
