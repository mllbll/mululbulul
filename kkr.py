# letters = 'СВЕТЛАНА'
# words = list(map(lambda x: ''.join(x), itertools.permutations(letters, 8)))
# count = 0
# for word in words:
#     if 'АА' not in word:
#         count+=1
# print(count)


# def f(n):
#     line=''
#     while n>0:
#         line+=str(n%5)
#         n=n//5
#     return line[::-1]
# ch=3*125**6+2*25**9+5**12-625
# print(f(ch))
# print(f(ch).count('0'))
# print(int('10000000444444440000',5)==ch)
# letters = 'СВЕТЛАНА'
# words = list(map(lambda x: ''.join(x), itertools.permutations(letters, 8)))
# count = 0
# for word in words:
#     if 'АА' not in word:
#         count+=1
# print(count)


# maxx=0
# buff=0
# for sign in range(201,2000):
#     line='1'*sign
#     while '1111' in line:
#         line=line.replace('1111','22',1)
#         line=line.replace('222','1',1)
#     if line.count('1')>maxx:
#         maxx=line.count('1')
#         buff=sign
# print(buff)


# st = []
# with open('file.txt', 'r') as f:
#     for line in f:
#         for i in '.,!?:;()':
#             line = line.replace(i, '')
#         line = line.lower()
#         st.extend(line.split())
#
# dct = {}
# for elem in st:
#     if dct.get(elem) != None:
#         dct[elem] += 1
#     else:
#         dct.update([(elem, 1)])
#
# res = sorted(dct.items(), reverse=True)
# resx = [res[0][0]]
# for i in range(1, len(res)):
#     if res[i][1] == res[i - 1][1]:
#         resx.append(res[i][0])
#
# resx = sorted(resx)
# print(resx[0])

# n = int(input())
#
# st = []
#
# for i in range(n):
#     a = int(input())
#     st.append(a)
#
# min_square = []
#
# for elem in range(0, len(st)-5-1):
#     for elem2 in range(elem+5, len(st)-1):
#         min_square.append((st[elem]**2)+(st[elem2]**2))
#
# print(min(min_square))
def F_2(n):
    F_2 = []
    for sign in range(1, n + 1):
        if sign % 2 == 0:
            F = 2 * sign
            F_2.append(F)
    return F_2
