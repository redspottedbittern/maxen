
class Tester():

    def __init__(self):
        self.one = 'haus'
        self.two = 'bein'

    def __getitem__(self, name):
        if name == 'one':
            return self.one
        elif name == 'two':
            return self.two

    def fun(self, name):

        return self[name]

    def giveme(self):
        g = input("Give me!")
        return g


def myfun(x):

    if x > 5:
        print("1")
    elif x > 3:
        print("2")
    else:
        print("3")


def whilefunc():

    wort = ["h", "u", "n", "d"]
    x = ''

    while x != 'hund':
        print("ungleich", x)
        x += wort.pop(0)


def inputtest(tester):
    return tester.giveme()
