import sys
D = {5: 10, 20: 10, 50: 10}
AllMoney = 5*D[5] + 20*D[20] + 50*D[50]
mon5 = 50
mon20 = 200
mon50 = 500



#D.update({5: Q, 20: Q, 50: Q, 100: Q})

a = int(input('Введите сумму: '))
if a > AllMoney:
    print('В банкомате нет столько денег')
    sys.exit()
else:
    AllMoney = AllMoney - a


money = 0

while money != a:
    if a >= mon5:
        new5 = 0
        D.update({5: new5})
        money = money + mon5

    elif a < mon5:
        new5 = int((mon5 - a) / 5)
        D.update({5: new5})
        money = a
        break

    if (a - money) >= mon20:
        new20 = 0
        D.update({20: new20})
        money = money + mon20

    elif (a - money) < mon20:
        new20 = int(10 - ((a - money)/20))
        D.update({20: new20})
        money = a
        break


    if (a - money) >= mon50:
        new50 = 0
        D.update({50: new50})
        money = money + mon50

    elif (a - money) < mon50:
        new50 = int(10 - ((a - money)/50))
        D.update({50: new50})
        money = a
        break

print("Получено денег:", a)
for b in D:
    print(b, "осталось", D[b])
