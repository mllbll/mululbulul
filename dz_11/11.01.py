class array(object):
    def __init__(self, a, b, lst, lst_1):
        self.lst = lst
        self.lst_1 = lst_1
        self.a = a
        self.b = b
        super().__init__()

    def updating(self):
        self.lst.append(a)
        return self.lst

    def deleting(self):
        self.lst.remove(b)
        return self.lst

    def multiplication(self):
        self.lst_answ = [int(i) * int(j) for i in lst for j in lst_1]
        return self.lst_answ

    def clearing(self):
        self.lst_new = []
        return self.lst_new

    def uniq(self):
        return (len(set(self.lst)))

def intovanie(n):
    for sign in range(len(n)):
        n[sign] = int(n[sign])
    return n
lst = intovanie(input('Введите список(числа через пробел) : ', ).split())
number = int(input('Введите номер операции : ', ))
if __name__ == "__main__":
    if number == 1:
        a = int(input('Введите число которое нужно добавить : ', ))
        arr = array(a, 0, lst, 0)
        print(arr.updating())
    if number == 2:
        b = int(input('Введите число которое нужно удалить : ', ))
        arr = array(0, b, lst, 0)
        print(arr.deleting())
    if number == 3:
        lst_1 = intovanie(input('Введите второй список(числа через пробел) : ', ).split())
        arr = array(0, 0, lst, lst_1)
        print(arr.multiplication())
    if number == 4:
        arr = array(0, 0, lst, 0)
        print(arr.clearing())
    if number == 5:
        arr = array(0, 0, lst, 0)
        print(arr.uniq())