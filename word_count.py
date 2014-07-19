__author__ = 'Андрюха'
import sys

filename = sys.argv[1]




def spliter(filename):
    n=0
    fr = open(filename)
    for i in fr:
        split_line = [s for s in i.split(' ') if s and s != '\n'] # разделяем строку по разделителю исключая перевод строки и пустую строку
        n+=len(split_line)
    print (n)

if __name__=='__main__':
    spliter(filename)

