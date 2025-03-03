import sys
import statgen
import teacher
import graph_gen

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <excel_file.xlsx> <first_column> <end_column>")
        print("<first_column> - номер первого столбца, связанного с этим предметом")
        print("<end_column> - номер последнего столбца (включительно), связанного с этим предметом")
    else:
        file_name = sys.argv[1]
        start_column = int(sys.argv[2])
        end_column = int(sys.argv[3])
        
        stat_gen = statgen.statgen(file_name, start_column, end_column)
        stat_gen.parse_columns(2, 3)
        stat_gen.parse_and_join_columns(4, 9)
        stat_gen.parse_teachers("Лектор")
        i = 1
        for key, value in stat_gen.general.items():
            graph_gen.generate_graph_numbers(value, 66, key, f"{i}")
            i += 1
        #for i in range(2, 10):
        #    stat_gen.print_column_statistic(i)
        # znamka = teacher.lecturer(stat_gen.sheet, 11, 21, "Знаменская Л.Н.")
        # znamka.parse_questions()
        #znamka.print_questions()
        #znamka.parse_marks()
    #     znamka.print_marks()
        #import pdb; pdb.set_trace()
       #  znamka.parse_comments()
       # # znamka.print_comments()
        # for i in znamka.marks:
        #     graph_gen.generate_graph_numbers(znamka.marks[i], 67, i)
        #stat_gen.find_categories()
        # ifor i in range(2, 30):
        #     stat_gen.print_column_stat(i)
