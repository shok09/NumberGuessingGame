from random import randint

min = 1
max = 100
tries = 7
number = randint(min, max)
while(True):
    print(f"Доброго здоров'ячка! Я загадав число від {min} до {max}. Спробуйте вгадати його за {tries} спроб")
    guess = 0
    for i in range(1, tries):
        guess = int(input("Введіть ваше припущення: "))
        if(guess > number):
            print("Обране число занадто велике!")
        elif(guess < number):
            print("Обране число занадто маленьке!")
        else:
            print(f"Ви вгадали! Це число {number}!")
            break
    if(number != guess):
        print(f"Мені дуже прикро це казати, але, на превеликий жаль, вам не вдалося відгадати число за {tries} спроб.\nЗагадане число: {number}")
    print("Бажаєте зіграти ще раз? (y/n)")
    answer = ""
    while(answer != "n" and answer != "y" and answer != "ні" and answer != "так"):
        answer = input("Введіть n (ні) або y (так): ").lower()
    if(answer == "n" or answer == "ні"):
        break
print("До побачення! Чекатиму з нетерпінням на ваше повернення!")
