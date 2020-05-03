def sort_negatives(*args):
    pos_vars = []
    neg_vars = []

    for i in range(len(args)):
        if int(args[i]) >= 0:
            pos_vars.append(args[i])
        else:
            neg_vars.append(args[i])

    # Sort negative array
    neg_vars.sort()
    # Append not touched positive array
    neg_vars.extend(pos_vars)

    return neg_vars

