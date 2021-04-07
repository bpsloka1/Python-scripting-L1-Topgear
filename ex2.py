'''

Implement the function isWhiteLine(), which takes a string and returns TRUE if the
string contains only white space & tab characters.

Making use of the above function, write a program, which should read a file given as
command-line argument, and print only non-blank lines onto the standard output.

'''
def isWhiteLine(string):
    if (type(string) == str):
        l = len(string)
        i = 0
        ws = 0
        nws = 0
        s1 = ''
        while(i<l):   ## validate each string 
            if( (string[i] == ' ') or (string[i] == '\t')):
                 ws += 1
            else:
                nws += 1
                s1 += string[i]
            i += 1
        if(nws == 0):
            return 'TRUE'
        else:
            return s1

try:  ### to check if file input is given properly or not
    
    ## program beginning 
    file_path = input('Please enter file path or directorty of text file to be read : ')  ## file path input
    f = open(file_path , 'r')
    op = isWhiteLine(f.read())  ## function called
    print(op)
except FileNotFoundError :
    print('''\nPlease enter full valid text file path     \n  Example 1: C:\\Users\\dell\\practice1.txt  or \n  Example 2 practice1.txt \nPlease mention '.txt' at the end ''' )
