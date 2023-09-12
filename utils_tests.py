from utils import *

#test function reversed
def reversed_test(input):
    test = utils()
    try:
        print(test.reversed(input))
    except:
        print('wrong input type, error')
#test function formatter
def formatter_test(input):
    test = utils()
    try:
        print(test.formatter(input))
    except:
        print('wrong input type, error')

if __name__=='__main__':
    str = 'string'
    int = 1234
    float = 12.34
    reversed_test(str)
    reversed_test(int)
    reversed_test(float)
    formatter_test(str)
    formatter_test(int)
    formatter_test(float)

