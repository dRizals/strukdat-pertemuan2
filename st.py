#program untuk membalik kata
def push(s, data):
    s.append(data)
    return (s)

def pop(s):
    data=s.pop()
    return(data)
    
kata= input('masukkan kata= ')
st=[]
hasil=''
for i in range(len(kata)):
     push(st, kata[i])

for i in range(len(kata)):
    hasil=hasil+pop(st)
print(hasil)
