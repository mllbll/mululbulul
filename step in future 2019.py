# n=input()
# ch=[]
# lst={}
# lsttt=[]
# for sign in range(0,len(n)):
#     ch.append(n[sign])
# for mark in range(len(ch)):
#     num=abs(int(ch[mark]) - (mark+1))
#     l={num:mark+1}
#     lst.update(l)
#     lsttt.append(num)
# lsttt.sort()
# print(lst.get(lsttt[-1]))
n=int(input())
line=bin(n)[2:]
print(line)
print(len(line))
