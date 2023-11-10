j = int(input('masukkan jumlah perulangan: '))
for b in range(j):
    a = input('masukkan kata : ')
    for i in range (len(a)-1):
        if (ord(a[i])-ord(a[i+1])) < 0:
            print(a[i], 'kurang dari', a[i+1], 'selisihnya ialah', -(ord(a[i])-ord(a[i+1])))
        elif (ord(a[i])-ord(a[i+1])) > 0:
            print(a[i], 'lebih dari',a[i+1], 'selisihnya ialah', (ord(a[i])-ord(a[i+1])))
        else:
            print(a[i], 'sama dengan', a[i+1], 'selisihnya ialah', (ord(a[i])-ord(a[i+1])))














    



    





