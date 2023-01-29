def fusion(L1: list, L2: list)->list:
    T = []
    P1 = 0
    P2 = 0
    while P1 != len(L1) and P2 != len(L2):
        if P1 > len(L1)-1:
            T.append(L2[P2])
            P2 += 1
        elif P2 > len(L2)-1:
            T.append(L1[P1])
            P1 += 1
        elif L1[P1] > L2[P2]:
            T.append(L2[P2])
            P2+=1
        else:
            T.append(L1[P1])       
            P1+=1
    T.append(L1[P1])
    return T 



def fusion_rec(L1: list, L2: list)->list:
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    elif L1[0] <= L2[0]:
        a = L1.pop(0)
        return [a] + fusion_rec(L1, L2)
    else:
        a = L2.pop(0)
        return [a] + fusion_rec(L1 , L2)

def tri_fusion(L):
    if len(L) == 1:
        return L
    else:
        return fusion_rec(tri_fusion(L[:len(L)//2]) ,tri_fusion(L[len(L)//2:]) )

L1 = [11, 16, 18, 99]
L2 = [5,6,7, 86]
print(fusion(L1,L2))
print(fusion_rec(L1,L2))

a = [8,1,3,2,5]
b = [8,1,3,2,5,9]
print(tri_fusion(a))
print(tri_fusion(b))
