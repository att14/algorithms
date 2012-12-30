def sort(unsorted):
    if len(unsorted) == 1:
        return unsorted

    length = len(unsorted)
    left, right = unsorted[:length/2], unsorted[length/2:]

    left = sort(left)
    right = sort(right)

    return merge(left, right)


def merge(left, right):

    def first(l):
        return l[0]

    result = []

    while len(left) or len(right):
        if len(left) and len(right):
            if first(left) <= first(right):
                result.append(first(left))
                del left[0]
            else:
                result.append(first(right))
                del right[0]
        elif len(left):
            result.append(first(left))
            del left[0]
        elif len(right):
            result.append(first(right))
            del right[0]

    return result
