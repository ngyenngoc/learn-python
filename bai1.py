a=10
b=15
t=a+b
print("gia tri phep cong t la",t)
t=a-b
print("gia tri phep tru t la",t)
t=a//b
print("gia tri phep chia lay phan nguyen t la",t)
t=a%b
print("gia tri chia lay phep du t la",t)
if a>b:
    print("so lon hon la",a)
    print("so be hon la",b)
else:
    print("so lơn hon la",b)
    print("so be hon la ",a)
print("in ra mot dong la:",str(a)+str(b))
if a<b:
    for n in range (a+1,b):
     print(n)
else:
    print("a phai nho hon b")
    