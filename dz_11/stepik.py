# # # # lst = []
# # # #
# # # #
# # # # def perev(n):
# # # #     line = list(n)
# # # #     for sign in range(len(line)):
# # # #         if line[sign] == '0':
# # # #             line[sign] = '1'
# # # #         else:
# # # #             line[sign]='0'
# # # #     return ''.join(line)
# # # #
# # # # def summa(n):
# # # #     s=0
# # # #     while n>0:
# # # #         s+=n%10
# # # #         n=n//10
# # # #     return s
# # # #
# # # #
# # # # # for sign in range(1000):
# # # #     line = bin(sign)[2:]
# # # #     if summa(sign)%2==0:
# # # #         line=line + '0'
# # # #     else:
# # # #         line=line + '1'
# # # #     if summa(sign)%2!=0:
# # # #         line=line + '0'
# # # #     else:
# # # #         line=line + '1'
# # # #     if summa(sign)%2!=0:
# # # #         line=line + '0'
# # # #     else:
# # # #         line=line + '1'
# # # #     r=int(line,2)
# # # #     if r>1028:
# # # #         print(r)
# # # #         lst.append(r)
# # # # lst.sort()
# # # # print('>>>>>><<<<<<<')
# # # # print(lst)
# # # a = {0: "У", 1: "О", 2: "А"}
# # # k = 0
# # # for i in range(0, len(a)):
# # #     for j in range(0, len(a)):
# # #         for g in range(0, len(a)):
# # #             for m in range(0, len(a)):
# # #                 for n in range(0, len(a)):
# # #                     k += 1
# # #                     if k == 100:
# # #                         print(a[i], a[j], a[g], a[m], a[n], end=" ")
# # count=0
# # # for sign in range(8**3,8**4):
# # #     line=oct(sign)[2:]
# # #     if int(line)%4==0:
# # #         count+=1
# # # print(count)
# # def per(n):
# #     count=0
# #     while n > 0:
# #         if n%17==16:
# #             count+=1
# #         n=n//17
# #     return(count)
# # # line=17**5+85**8-10
# # # print(per(line))
# # # Автомат получает на вход четырёхзначное натуральное число и строит новое число по следующему алгоритму:
# # # 1. вычисляются суммы первой и второй, второй и третьей и третьей и четвёртой цифр;
# # # 2. из полученных сумм отбрасывается наименьшая;
# # # 3. остальные суммы записываются в порядке неубывания.
# # # Пример. Исходное число:1284. Суммы: 1 + 2 = 3; 2 + 8 = 10; 8 + 4 = 12. Отбрасывается наименьшая сумма 3.
# # # Результат: 1012. Укажите наименьшее число, при вводе которого автомат выдаёт значение 1316.
# #
# # def stroki(n):
# #     s=''
# #     for sign in range(len(n)):
# #         s+=str(n[sign])
# #     return s
# #
# # lass=['1','2','3','4','5','6','7','8','9','0']
# # # print(stroki(lass))
# #
# # for sign in range(1000,9999+1):
# #     lst=[]
# #     line=list(str(sign))
# #     s1=int(line[0]) + int(line[1])
# #     s2=int(line[1]) + int(line[2])
# #     s3=int(line[2]) + int(line[3])
# #     lst.append(s1)
# #     lst.append(s2)
# #     lst.append(s3)
# #     lst.sort()
# #     lst.pop(0)
# #     l=stroki(lst)
# #     if int(l)==210:
# #         print(sign)
#
# # for sign in range(6,7):
# #   line=bin(sign)[2:]
# #   if line.count('1')%2==0:
# #     line='10' + line[2:] +'0'
# #   else:
# #     line='11' + line[2:] + '1'
# #   r=int(line,2)
#
# # s = []
# # for a1 in range(1, 200):
# #   for a2 in range(1, 200):
# #     fl = True
# #     for x in range(1, 200):
# #       if not ((130 <= x <= 171) <= (((150 <= x <= 185) and (not (a1 <= x <= a2))) <= (not (130 <= x <= 171)))):
# #         fl = False
# #         break
# #     if fl:
# #       s.append(a2 - a1)
# # print(min(s))
#
#
# # for a in range(300, 0, -1):
# #     k = 0
# #     for x in range(0, 300):
# #         for y in range(0, 300):
# #             for z in range(0, 300):
# #                 if (5*y + 2 * x + 4 * z!= 80) or (a < 6*x) or (a < y) or (a < 3*z):
# #                     k += 1
# #     if k == 90_000:
# #         print(a)
# #         break
#
# # print("a b c d")
# # for a in range(0, 2):
# #     for b in range(0, 2):
# #         for c in range(0, 2):
# #             for d in range(0, 2):
# #                 if not(a and not b or (a or b) and c or d):
# #                     print(a, b, c, d)
#
#
# # for A in range(1,1000):
# #     B = True
# #     for x in range(1,1000):
# #         if not((x&43==0) or (not (x&49==0) or (x&A!=0))):
# #             B=False
# #     if B:
# #         print(A)
# #         break
#
# def cifri(n):
#     s=[]
#     while n > 0:
#         s.append(int(n%10))
#         n=n//10
#     return sorted(s,reverse=True)
#
#
# def f(n):
#     s=''
#     for i in range(len(n)):
#         s+=str(n[i])
#     return s
#
# for sign in range(3165,10000):
#     ls=[]
#     line=cifri(sign)
#     s1=line[0] + line[1]
#     s2=line[2] + line[3]
#     ls.append(s1)
#     ls.append(s2)
#     ls=sorted(ls,reverse=True)
#     s=int(f(ls))
#     if s==1512:
#         print(sign)
#         break
# with open('26.txt') as F:
#     f=F.read()
# lst=f.split('\n')
# for sign in range(len(lst)):
#     lst[sign]=list(lst[sign].split(' '))
#
# print(lst)
# import itertools
# alphabet = "АББАТИСА"
# vol = "АИ"
# con = "БТС"
# ar = itertools.permutations(alphabet, 8) #Размещение
# arl = []
# for e in ar:
#     arl.append(list(e))
# a = set()
# for e in arl:
#     flag = True
#     s = ""
#     for i in range(len(e)-1):
#         s += e[i]
#         if (e[i] in vol and e[i+1] in vol) or (e[i] in con and e[i+1] in con):
#             flag = False
#     if flag:
#         a.add(s)
# print(len(a))
# import re
#
# with open('k7b-1.txt', 'r') as f:
#     txt = f.read()
# print(len(max(re.findall(r'(?m)(EAB)+(EA|E)?', txt), key=len)))

for a in range(50,0,-1):
    flag=0
    for x in range(100):
        for y in range(100):
            for z in range(100):
                if ((156!=4*y+x**2+3*z)or (a<8*x**2) or (a<y) or (a<4*z))==0:
                    flag=1
    if flag==0:
        print(a)