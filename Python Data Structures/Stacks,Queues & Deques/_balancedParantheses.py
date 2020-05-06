def balance_check(s):
    if len(s)%2 != 0:
        return False
    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for p in s:
        if p in opening:
            stack.append(p)
        else:
            if len(stack)==0:
                return False
            last_open = stack.pop()
            if (last_open,p) not in matches:
                return False
    return len(stack)==0

def main():
    b = balance_check('[]')
    c = balance_check('[')
    d = balance_check('[](){([[[]]])}')
    e = balance_check('[](){([[[]])}')
    print (b)
    print (c)
    print (d)
    print (e)

if __name__ == "__main__":
    main()