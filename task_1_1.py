d=int(input('Введите любое число  '))
day=d//86400
d1=d%86400
h=d1//3600
h1=d1%3600
m=h1//60
m1=h1%60
s=m1
print(day, 'дней', h, 'часов', m, 'минут', s, 'секунд')