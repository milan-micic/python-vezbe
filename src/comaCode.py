spam = ["bananas", 1, "apples"]


def joinAllListItems(arr):
    """
    Purpose: Join all items in list and separete items with space and coma,with 'end' before last item
      @param arr list: Any array include zero array or mix integers and strings
      @return string
    """

    if len(arr) > 1:
        arr = [str(element) for element in arr]
        res = ", ".join(arr[:-1]) + " and " + arr[-1]
    elif len(arr) == 0:
        return "Vas niz je prazan!"
    else:
        res = arr[0]
    return res


print(joinAllListItems(spam))
