a = [2, 4, 6, 9, 7]
chan = 0
le = 0

for x in a:
    if x % 2 == 0:
        chan += 1
    else:
        le += 1

print("Số chẵn:", chan)
print("Số lẻ:", le)