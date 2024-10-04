# 构建不排序的C函数
def C(t,m,n):
    a=[]
    b=[]
    c=[]
    x=[]
    if m>=n:
        for i in range(n-2,m-1):
            b=t[i-n+2:i+1]
            c=t[i+1:]
            for j in range(len(c)):
                x=b[:]
                x.append(c[j])
                a.append(x)
    return a


# 判断集合包含关系
def pdbaohan(a,b,n):
    for j in b:
        flag=0
        for i in a:
            for k in range(len(j)):
                if j[k]==i:
                    flag=flag+1
        if flag>=n:
            return 1
    return 0

# 判断所给彩票是否可以必定中奖
def pdcaipiao(t,n,answer,k):
    s=C(t,len(t),n)
    flag=0
    for i in s:
            if pdbaohan(i,answer,k):
                flag=flag+1
    if flag==len(s):
        return 1
    else:
        return 0


t=[int(i) for i in input().split()]
m=len(t)
n,k=map(int,input().split())
print(n,k)


SHUDUI=C(t,m,k)
answerlist=[]
for i in SHUDUI:
    t2=t[:]
    for j in i:
        t2.remove(j)
    S=C(t2,len(t2),n-k)
    for j in S:
        answer=j+i
        if pdbaohan(answer,answerlist,k):
            continue
        else:
            answerlist.append(answer)


print(answerlist)
print(pdcaipiao(t,n,answerlist,k))
