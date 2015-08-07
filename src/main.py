# dummy main
import lcd_generator as lcd

def main():
    print "ICFP 2015"

    # test of random sequence generator for the example from the documentation
    unit_indizes = lcd.generate_random_sequence(17,10)
    print unit_indizes


if __name__ == "__main__":
    main()