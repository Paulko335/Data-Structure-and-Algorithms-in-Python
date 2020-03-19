# Four string composition methods in section 5.4.2

def func1(document):
    letters = ""
    for c in document:
        if c.isalpha():
            letters += c
    return letters

def func2(document):
    temp = []
    for c in document:
        if c.isalpha():
            temp.append(c)
    letters = "".join(temp)
    return letters

def func3(document):
    letters = "".join([c for c in document if c.isalpha()])
    return letters

def func4(document):
    letters = "".join((c for c in document if c.isalpha()))
    return letters

