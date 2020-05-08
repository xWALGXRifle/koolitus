def bp(list, items):
    list.append(items)
    return list


def update(old, new):
    for x in new:
        old.append(x)
    return old