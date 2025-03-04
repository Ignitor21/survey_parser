import matplotlib.pyplot as plt
import os

def generate_graph_numbers(statistic : dict, total_amount : int, title : str, filename : str):
    # Создание столбчатой диаграммы
    categories = list(statistic.keys())
    values = []
    if all(type(item) == str for item in categories):
        categories = [cat.replace(' ', '\n') for cat in categories]
        values = list(statistic.values())
    else:
        categories = list(range(1, 11))
        for mark in categories:
            if mark not in statistic.keys():
                values.append(0)
            else:
                values.append(statistic[mark])

    plt.figure(figsize=(16, 9)) 
    bars = plt.bar(categories, values, color = 'RoyalBlue', width = 0.5)

    # Добавление подписей к столбцам
    for bar in bars:
        height = bar.get_height()
        if height != 0:
            plt.text(bar.get_x() + bar.get_width() / 2, height * 0.5 , f'{height}', ha = 'center', fontsize = 12, bbox = dict(facecolor = 'white', alpha = .3))

    # Настройки графика
    plt.title(title, fontsize = 14)
    plt.tick_params(axis = 'both', labelsize = 14)
    if any(type(item) == int for item in categories):
        plt.xticks(range(0, 11))
        
    filepath = os.path.join('images', f'{filename}.png')
    plt.savefig(filepath, dpi = 300, bbox_inches='tight')  # bbox_inches='tight' обрезает лишние поля
    #plt.show()
    plt.close()  # Закрываем фигуру, чтобы освободить память


#Test
# categories = ['Смотрел \n лекции', 'Посещал \n лекции', 'Посещал \n семинары', 'Читал \n литературу', 'Читал конспекты \n лекций лектора', 'Другое']
# values = [38, 50, 65, 43, 43, 5]
# statistic = dict(zip(categories, values))
# title = "Какими материалами Вы пользовалилсь при изучении курса?"
# generate_graph_numbers(statistic, 66, title, "test")
