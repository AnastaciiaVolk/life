__author__ = 'Андрюха'
import sys

filename = sys.argv[1]




def spliter(filename):
    n=0
    fr = open(filename)
    for i in fr:
        split_line = i.split(' ')
        n+=len(split_line)
    print (n)

if __name__=='__main__':
    spliter(filename)

