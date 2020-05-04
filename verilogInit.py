def initiater(i):
    if i == 0:
        print ("",end = "\t")
    else: print ("#10",end = "\t")
def print_digit(x, index):
    d = size-1 - index
    print ("{0}<={1};".format(x,digit[d]),end="\t")
    if x == L[-1]:
        change_digit(0)
def change_digit(d):
    if d == size:
        return
    digit[d] = (digit[d] + 1) % 2
    if digit[d] == 0:
        change_digit(d+1)

L = input().split()
size = len(L)
digit = [0]*size
for i in range (2**size):
    index = 0
    initiater(i)
    for k in L:
        print_digit(k,index)
        index += 1
    print("")