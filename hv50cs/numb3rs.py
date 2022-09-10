"""
  Use of regular expressions for validating an IP Address
  patterns and strings to be searched can be Unicode strings (str)
   as well as 8-bit strings (bytes), cannot be mixed.

  backslash character ('\') indicates special forms
   or allow special characters to be used without invoking their special meaning.

   Usually patterns will be expressed in Python code using this raw string notation.

   most regular expression operations are available as module-level functions and methods
    on compiled regular expressions. The functions are shortcuts that don’t require you
    to compile a regex object first, but miss some fine-tuning parameters.

    There is also a third-party regex module.

    A RE specifies a set of strings that matches it.
    The moduleś functions check if a particular string matches a given regular expression
     or if a given regular expression matches a particular string.

    Regular expressions can be concatenated to form new regular expressions

    Regular expression patterns are compiled into a series of bytecodes
     which are then executed by a matching engine written in C.

    The regular expression language is relatively small and restricted,
      so not all possible string processing tasks can be done using regular expressions.
      There are also tasks that can be done with regular expressions,
      but the expressions turn out to be very complicated. 
      In these cases, you may be better off writing Python code to do the processing;
      while Python code will be slower than an
      elaborate regular expression, it will also probably be more understandable.

    For a detailed explanation of the computer science underlying 
    regular expressions (deterministic and non-deterministic finite automata), 
    you can refer to almost any textbook on writing compilers.

    metacharacters: 
    metacharacters: . ^ $ * + ? { } [ ] \ | ( )

    Explanation:  

    1- character class [] a set of characters that you wish to match.

    Listed individually, or a range of characters giving two characters separated by a '-'.
      For example, [abc] or [a-c] will match any of the characters a, b, or c;
      [a-z] match only lowercase letters.

    Recall that the re module comes with quite a few functions, 
    per docs.python.org/3/library/re.html, including search.
    Recall that regular expressions support quite a few special characters, 
    per docs.python.org/3/library/re.html#regular-expression-syntax.
    Because backslashes in regular expressions could be mistaken for escape sequences (like \n),
    best to use Python’s raw string notation for regular expression patterns, 
    else pytest will warn with DeprecationWarning: invalid escape sequence. 

    Just as format strings are prefixed with f, so are raw strings prefixed with r.
    For instance, instead of "harvard\.edu", use r"harvard\.edu".
    Note that re.search, if passed a pattern with “capturing groups” 
    (i.e., parentheses), returns a “match object,” 
    per docs.python.org/3/library/re.html#match-objects, 
    wherein matches are 1-indexed, which you can access individually with group, 
    per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, 
    per docs.python.org/3/library/re.html#re.Match.group
      
      

"""
import re
import sys

def main():
    print(validate_ipv4(input("IPv4 Address: ")))

def part_valid(p):
    if p >= 0 and p <= 255:
        return True
    else:
        return False

def validate_format(ip_address):
    #r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)
    if not re.search(ip_address,"r^[0-9]\."):
        print(f"Validate_format: Formato no valido {ip_address}")
        return False
    else:
        print(f"Validate_format: Formato valido {ip_address}")
        return True
    
def validate_ipv4(ip_address):
    if not validate_format(ip_address):
        return False
    try:
         p1, p2, p3, p4 = ip_address.split(".")

         print(f"Componentes : {p1}:{p2}:{p3}:{p4}")

         if part_valid(int(p1)) and part_valid(int(p2)) and part_valid(int(p3)) and part_valid(int(p4)):
            return True
         else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()