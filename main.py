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
        
        stat_gen.parse_and_graph_general()
        stat_gen.parse_and_graph_lecturers()
        stat_gen.parse_and_graph_seminarists()
        stat_gen.parse_and_graph_labniks()
