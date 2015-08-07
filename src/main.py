# dummy main
import lcd_generator as lcd
import handlejson
import unit

def main():
    print "ICFP 2015"

    # test JSON parser
    problem_dict = handlejson.parse_to_dictionary(handlejson.data)

    # create a units
    units = [unit.Unit(u) for u in problem_dict['units']]

    for u in units:
        print u
        print "-------------------------"


    # test of random sequence generator for the example from the documentation
    unit_indizes = lcd.generate_random_sequence(17,10)
    print unit_indizes


if __name__ == "__main__":
    main()