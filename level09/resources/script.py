l = "66346b6d6d36707c3d827f70826e838244428344757b7f8c890a"

bt = bytes.fromhex(l)

res = bytearray(bt)

for i, n in enumerate(bt):
    res[i] = (n - i) % 256
print(res)    
#print(res.decode('utf'))    

