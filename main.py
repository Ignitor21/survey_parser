import sys
import statgen
import teacher

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <имя_файла.xlsx>")
    else:
        file_name = sys.argv[1]
        statistic_generator = statgen.statgen(file_name)
        #import pdb; pdb.set_trace()
        for i in range(2, 10):
            statistic_generator.print_column_statistic(i)
        znamka = teacher.lecturer(statistic_generator.sheet, 11, 21, "Знаменская Л.Н.")
        znamka.parse_questions()
        znamka.print_questions()
        znamka.parse_marks()
        znamka.print_marks()
        znamka.parse_comments()
        znamka.print_comments()
        #statistic_generator.find_categories()
        # ifor i in range(2, 30):
        #     statistic_generator.print_column_stat(i)
