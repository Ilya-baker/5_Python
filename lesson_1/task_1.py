#https://drive.google.com/file/d/1RX-dh1_wvw-gvdxACC6ctwF-y2HSVgXl/view?usp=sharing
a = int(input('Введите любое целое положительное трёхзначное число: '))

b = a//100 + (a//10%10) + a%10
c = (a//100) * (a//10%10) * (a%10)

print(b)
print(c)