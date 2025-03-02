import openpyxl
import re

# Абстрактный класс
class teacher:
    def __init__(self, sheet, start_column : int, end_column : int, name : str):
        self.sheet = sheet
        self.start_column = start_column
        self.end_column = end_column
        self.name = name
        self.questions = {}
        self.marks = {}
        self.comments = []
    
    def parse_questions(self):
        pass

    def parse_marks(self):
        pass

    def parse_comments(self):
        pass

class lecturer(teacher):
    def parse_questions(self):
        
        questions_statistic = {}

        for column_index in range(self.start_column, self.end_column + 1):
            question_answers = 0
            #import pdb; pdb.set_trace()
            question = self.sheet.cell(1, column_index).value

            if question.startswith("Посещали ли Вы лекции?"):
                row_number = 2
                for row in self.sheet.iter_rows(min_row=2, min_col=column_index, max_col=column_index, values_only=True):
                    if (row[0] is not None) and (self.sheet.cell(row_number, self.start_column).value == self.name):
                        question_answers += 1
                    row_number += 1
                questions_statistic[question] = question_answers
        self.questions = questions_statistic
    
    def print_questions(self):
        for elem in self.questions:
            print(f"{elem} {self.questions[elem]}\n")

    def parse_marks(self):
        
        questions_statistic = {}

        for column_index in range(self.start_column, self.end_column + 1):
            question_answers = 0
            #import pdb; pdb.set_trace()
            question = self.sheet.cell(1, column_index).value

            if question.startswith("Оцените качество преподавания лекций"):
                row_number = 2
                for row in self.sheet.iter_rows(min_row=2, min_col=column_index, max_col=column_index, values_only=True):
                    cur_lecturer_name = self.sheet.cell(row_number, self.start_column).value
                    cell_value = row[0]
                    if (cell_value is not None) and (cur_lecturer_name == self.name):
                        cell_value = int(cell_value)
                        if cell_value in questions_statistic:
                            questions_statistic[cell_value] += 1
                        else:
                            questions_statistic[cell_value] = 1

                    row_number += 1
                self.marks[question] = dict(sorted(questions_statistic.items()))

    def print_marks(self):
        for elem in self.marks:
            print(f"{elem}\n{self.marks[elem]}\n")

    def parse_comments(self):
        questions_answers = []

        column_index = self.end_column
        question = self.sheet.cell(1, column_index).value

        row_number = 2
        for row in self.sheet.iter_rows(min_row=2, min_col=column_index, max_col=column_index, values_only=True):
            cur_lecturer_name = self.sheet.cell(row_number, self.start_column).value
            cell_value = row[0]
            if (cell_value is not None) and (cur_lecturer_name == self.name):
                questions_answers.append(cell_value)
                row_number += 1
        self.comments = questions_answers

    def print_comments(self):
        for elem in self.comments:
            print(f"{elem}\n")
        
