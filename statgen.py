import openpyxl
from collections import defaultdict

class statgen:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(filename=file_path)
        self.sheet = self.workbook.active
        self.categories = set()

    def parse(self):

        # Словарь для хранения подсчётов по столбцам
        column_counts = defaultdict(lambda: defaultdict(int))

        # Проход по строкам и столбцам
        for row in self.sheet.iter_rows(values_only=True):  # Итерируемся по строкам
            for col_idx, cell_value in enumerate(row):  # Итерируемся по ячейкам в строке
                if cell_value is not None:  # Игнорируем пустые ячейки
                    column_counts[col_idx][cell_value] += 1

        # # Вывод результатов
        # for col_idx, counts in column_counts.items():
        #     print(f"Столбец {col_idx + 1}:")
        #     for value, count in counts.items():
        #         print(f"  {value}: {count} раз(а)")
        #     print()

    def find_categories(self):

        # Проход по ячейкам первой строки
        for cell in self.sheet[1]:  # sheet[1] возвращает первую строку
            if cell.value is not None:  # Игнорируем пустые ячейки
                self.categories.add(cell.value)

        print(self.categories)

    def get_statistic_in_column(self, column_number : int):
        value_counts = {}

        # Проход по ячейкам столбца, начиная со второй строки
        for row in self.sheet.iter_rows(min_row=2, min_col=column_number, max_col=column_number, values_only=True):
            cell_value = row[0]  # row[0] — значение ячейки в текущем столбце
            if cell_value is not None: # Игнорируем пустые ячейки
                if cell_value.isnumeric():
                    cell_value = int(cell_value)
                if cell_value in value_counts:
                    value_counts[cell_value] += 1
                else:
                    value_counts[cell_value] = 1

        sorted_value_counts = dict(sorted(value_counts.items()))
        return sorted_value_counts
    
    def print_column_statistic(self, column_number : int):
        name = self.sheet.cell(1, column_number).value
        distribution = self.get_statistic_in_column(column_number)
        print(f"{name}\n{distribution}\n")

    TEACHER_TYPES = ["Лектор", "Семинарист", "Преподаватель по лабораторным работам"]


#    def get_teacher_statistic(self, name : str, start_column : int, end_column : int):
        
