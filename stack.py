#stack() membuat stack baru
#push(data) menambah data dengan parameter 
#pop() menghapus data di top dan me-return data yg dihapus
#peek() mengecek data top
#isEmpety()mengecek stack kosong atau tidak
#siza() mengetahui jumlah data

s=[5,6,7,8]
def stack():
    
    return (s)
def push(s, data):
    s.append(data)
    return (s)
def pop(s):
    data=s.pop()
    return(data)
def peek(s):
    return(s[len(s)]-1)
def isEmpety(s):
    return(s==[])
def size(s):
    return(len(s))

#print(stack(), push(s, 9))
