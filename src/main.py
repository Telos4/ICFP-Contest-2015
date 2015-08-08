# dummy main
import lcd_generator as lcd
import handlejson
import data_structures
import data

def main():
    print "ICFP 2015"

    # test JSON parser
    problem_dict = handlejson.parse_to_dictionary(data.data19)

    # create a boardmanager
    boardmanager = data_structures.BoardManager(problem_dict)

    boardmanager.simulation(0)


if __name__ == "__main__":
    main()