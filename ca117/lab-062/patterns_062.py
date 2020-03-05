from re import findall
import sys



def date(s):
    pass

def phone(s):
    pass

def email(s):
    pass

def ldate(s):
    pass

def main():

    # Verify regular expressions are not overly long
    

    s = sys.stdin.read()

    datelist = findall(r'\b(?:\d|\d\d)(?:[/]|[-])(?:\d|\d\d)(?:[/]|[-])(?:\d\d)\b', s)
    print('Dates: {}'.format(datelist))

if __name__ == '__main__':
    main()
