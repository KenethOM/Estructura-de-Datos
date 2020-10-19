


def binary_search(value, l):
    middle_index = int(len(l)/2)
    middle = l[middle_index]

    if value == middle:
        return l.index(middle)

    elif value < min(l) or value > max(l):
        return "Value not found"

    elif value < middle:
        for i in l[:middle]:
            if i == value:
                return l.index(i)

    elif value > middle:
        for i in l[middle:]:
            if i == value:
                return l.index(i)

