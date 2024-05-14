import random

start = input('Ви запустили гру "Камінь, ножиці, папір". Для початку натисніть "+" або "-" для виходу')

if start == '+':
    print('Завантаження...')
    print("Завантаження завершено! Починаємо гру!")
    print("3...2...1...")
    print("Якщо хочете вийти натисніть '-' .")
    print("Хочете дізнатися рахунок натисніть '?'")
    user_ball = 0
    rand_ball = 0
    while True:
        user = input('Камінь-"к", Ножиці-"н" чи Папір-"п"?')
        list_play = ['к','н','п']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

