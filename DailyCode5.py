
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)


def cons(a, b):

    def list(pick):
        if pick == 1:
            return a
        elif pick == 2:
            return b
        else:
            raise ValueError

    return list

def car(list):
    return list(1)

def cdr(list):
    return list(2)

if __name__== "__main__":
    print(car(cons(1, 2)))
