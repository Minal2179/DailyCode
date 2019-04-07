def productList(list):
    '''
    Since 2 other arrays left and right used so Space complexity O(n)
    Initially calculate value of left and right and then finally for each index take product of these arrays
    :param list: list of numbers
    :return: product of array elements except self
    '''
    left = [1] * len(list)
    right = [1] * len(list)

    for i in range(1, len(list)):
        left[i] = left[i - 1] * list[i - 1]

    for j in range(len(list) - 2, -1, -1):
        right[j] = right[j + 1] * list[j + 1]

    for i in range(len(list)):
        list[i] = left[i] * right[i]

    return list

def productList_revised(list):
    '''
    Space complexity: O(1)
    Compute the left half and right half by creating a result array and temp variable that is computed for an index
    before the index to which the value gets multiplied
    :param list: list of numbers
    :return: product of array elements except self
    '''
    result = [1] * len(list)
    temp = 1
    for i in range(0, len(list)):
        result[i] *= temp
        temp *= list[i]
    temp = 1
    for i in range(len(list) - 1, -1, -1):
        result[i] *=temp
        temp *= list[i]
    return result


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    print(productList_revised(list))
    print(productList(list))

