def sumOfNumbers(alist, num):
    map = {}
    for i in range(len(alist)):
        complement = num - alist[i]
        if complement in map:
            return [complement, alist[i]]
        else:
            map[alist[i]] = complement
    return None


def sumOfNumbersBrute(alist, num):
    for i in range(0, len(alist) - 1):
        for j in range(i+1, len(alist)):
            if alist[i] + alist[j] == num:
                return [alist[i], alist[j]]
    return None


def sumOfNumbersTwoPass(alist, num):
    map = {}
    for i in range(len(alist)):
        map[alist[i]] = i
    print(map)
    for i in range(len(alist)):
        complement = num - alist[i]
        if complement in map.keys() and map[complement] != i:
            return [complement, alist[i]]
        else:
            map[alist[i]] = complement
    return None


if __name__ == "__main__":
    alist = [10, 15, 3, 7]
    print(sumOfNumbers(alist, 17))
    print(sumOfNumbersBrute(alist, 17))
    print(sumOfNumbersTwoPass(alist, 17))