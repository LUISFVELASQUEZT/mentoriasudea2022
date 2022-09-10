import re
import sys

def main():
    print(validate_something(input("Something: ")))


def validate_something(something):
    
    res=[]
    res = re.split("r[.]", something)
    #res = re.split("\s", something.replace("."," "),)
    for i in res:
        print(i)
    


if __name__ == "__main__":
    main()