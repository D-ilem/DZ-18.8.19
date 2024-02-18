
summa = 0
tickets = int(input("Введите количество билетов: "))
for age in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age > 0 and age < 18:
        summa == 0
    elif age >= 18 and age <= 25:
        summa += 990
    elif age > 25 and age < 101:
        summa += 1390
if summa == 0:
    print("Дети и милиционеры - бесплатно!")
else:
    print(f"Стоимость билетов:", summa, 'руб')

if tickets > 3:
    discount = summa / 100 * 10
    print(f"Ваша скидка:",  discount, "руб.")
    print('--------------------')
    print(f"Итого:", summa - discount, "руб.")

