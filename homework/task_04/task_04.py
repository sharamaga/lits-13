def calc_circles(in_data):

    def calc(text: str):
        cnt = 0
        for i in text:
            if i == '9':
                cnt += 1
            elif i == '8':
                cnt += 2
            elif i == '6':
                cnt += 1
            elif i == '4':
                cnt += 1
            elif i == '0':
                cnt += 1
        return cnt

    if type(in_data) is float:
        return 'ERROR'

    in_str = str(in_data)
    """ Need special care for negatives """
    if type(in_data) is int:
        return calc(in_str)
    else:
        if in_str.isdigit():
            return calc(in_str)
        else:
            return 'ERROR'
