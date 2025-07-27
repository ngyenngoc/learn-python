a=[2,1,7,4,9]
chan=0
le=0
a.sort()
print(a)
a.sort(reverse=True)
print(a)
so_chan =[]
for x in a:
    if x%2==0:
        so_chan.append(x)
        chan +=1
print("Các số chẵn là:", so_chan,"số chẵn",chan)  
so_le = []
for x in a:
    if x % 2 != 0:
        so_le.append(x)
        le+=1
print("Các số lẻ là:", so_le,"số lẻ",le)
tong=sum(a)
print("Tổng các phần tử là",tong)
print("Hoc bai")
import math
tich=math.prod(a)
print("tích các phần tử là",tich)