def sort_odd(in_data):
    odd_vars = []
    loc_in_data = in_data

    for i in loc_in_data:
        if int(i) % 2 != 0:
            odd_vars.append(i)

    odd_vars.sort()

    cnt = 0
    j = 0
    for i in loc_in_data:
        if int(i) % 2 != 0:
            loc_in_data[j] = odd_vars[cnt]
            cnt += 1
        j += 1

    return loc_in_data

