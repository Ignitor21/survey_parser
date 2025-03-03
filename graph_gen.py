import matplotlib.pyplot as plt

def generate_graph_numbers(statistic : dict, total_amount : int, title : str):
    
    # Создание столбчатой диаграммы
    categories = list(statistic.keys())
    values = list(statistic.values())
    plt.figure(figsize=(16, 9)) 
    plt.bar(categories, values, color = 'RoyalBlue', width = 0.5)
    plt.axhline(y = total_amount, color = 'silver', linestyle = '--', label = 'Общее количество опрошенных')
    plt.legend(loc = 'center right', bbox_to_anchor = (1, 0.9), fontsize = 14)

    # Добавление подписей к столбцам
    for i, value in enumerate(values):
        plt.text(i, value/2, str(value), ha = 'center', fontsize = 12, bbox = dict(facecolor = 'white', alpha = .3))

    # Настройки графика
    plt.title(title, fontsize = 14)
    plt.tick_params(axis = 'both', labelsize = 14)

    plt.savefig('/home/jorik/survey/images/001-image.png', dpi = 300, bbox_inches = 'tight')
    plt.show()

#Test
categories = ['Смотрел \n лекции', 'Посещал \n лекции', 'Посещал \n семинары', 'Читал \n литературу', 'Читал конспекты \n лекций лектора', 'Другое']
values = [38, 50, 65, 43, 43, 5]
statistic = dict(zip(categories, values))
title = "Какими материалами Вы пользовалилсь при изучении курса?"
generate_graph_numbers(statistic, 66, title)
