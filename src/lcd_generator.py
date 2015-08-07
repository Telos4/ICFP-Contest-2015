def generate_random_sequence(seed, sourceLength, units):
    """
    :param seed:            random seed
    :param sourceLength:    total number of units
    :param units:           number of unique units
    :return: list with indizes of units (spawn order)
    """

    m = 4294967296  # modulus (2^32)
    a = 1103515245  # multiplier
    c = 12345       # increment

    r = 2147483647  # relevant bits for random number (2^31 - 1)

    unit_indizes = [0 for i in xrange(sourceLength)]
    for i in xrange(0,sourceLength):
        # generate random number from the current seed
        unit_indizes[i] = ((r & seed) >> 16) % units

        # compute next seed
        seed = (a * seed + c) % m

    return unit_indizes