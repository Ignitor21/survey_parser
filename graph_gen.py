import matplotlib.pyplot as plt

def generate_graph_numbers(categories : list, values : list, total_amount : int):
    
    # Создание столбчатой диаграммы
    plt.figure(figsize=(16, 9)) 
    plt.bar(categories, values, color = 'RoyalBlue', width = 0.5)
    plt.axhline(y = total_amount, color = 'silver', linestyle = '--', label = 'Общее количество опрошенных')
    plt.legend(loc = 'center right', bbox_to_anchor = (1, 0.9), fontsize = 14)

    # Добавление подписей к столбцам
    for i, value in enumerate(values):
        plt.text(i, value/2, str(value), ha = 'center', fontsize = 12, bbox = dict(facecolor = 'white', alpha = .3))

    # Настройки графика
    plt.title('Какими материалами Вы пользовалилсь при изучении курса?', fontsize = 14)
    plt.tick_params(axis = 'both', labelsize = 14)

    plt.savefig('C:/Users/d.r.tikhonov/Documents/Reports/images/materials_matan_1.png', dpi = 300, bbox_inches = 'tight')
    plt.show()

# Test
# categories = ['Смотрел \n лекции', 'Посещал \n лекции', 'Посещал \n семинары', 'Читал \n литературу', 'Читал конспекты \n лекций лектора', 'Другое']
# values = [38, 50, 65, 43, 43, 5]

# generate_graph_numbers(categories, values, 66)
