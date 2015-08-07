# dummy main
import lcd_generator as lcd
import handlejson
import data_structures
import data

def main():
    print "ICFP 2015"

    # test JSON parser
    problem_dict = handlejson.parse_to_dictionary(data.data7)

    # create a boardmanager
    boardmanager = data_structures.BoardManager(problem_dict)

    boardmanager.simulation(0)


    # test of random sequence generator for the example from the documentation
    unit_indizes = lcd.generate_random_sequence(17,10,20)
    print unit_indizes


if __name__ == "__main__":
    main()