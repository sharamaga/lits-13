def check_symmetry(in_data):
    """ Format string at begging """
    """ Make all lower case"""
    loc_str = (str(in_data)).lower()
    """ Remove white spaces """
    loc_str = loc_str.replace(' ', '')
    """ Compare two cuts, second with reverse direction.
        Since reverse direction starts from -1 need add 1 to final index """
    if loc_str[0:int(len(loc_str) / 2):1] == loc_str[-1:-(int(len(loc_str) / 2) + 1):-1]:
        print('YES')
    else:
        print('NO')

    pass

