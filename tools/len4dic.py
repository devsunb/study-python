import string

for a in string.ascii_lowercase:
    print(a)
    for b in string.ascii_lowercase:
        print(a+b)
        for c in string.ascii_lowercase:
            print(a+b+c)
            for d in string.ascii_lowercase:
                print(a+b+c+d)