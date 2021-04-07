'''
Implementing function ruler() which takes a number as argument , and produces output as ruler
'''
### use from ex1 import ruler   - to use ruler function
def ruler(num):
    if ( type(num) == int ) :
        a = num % 10
        b = int(num/10)
        i = 1
        ## line 1
        l1 = ''
        while(i<(b+1)):
            l1 += '         ' + str(i)
            i+=1
        print(l1)
        ## line 2 recursive numbers from 1 to 9 and 0 
        ls2 = ''
        i = 1
        while(i<(b+1)):
            j=1
            while(j<10):
                ls2 += str(j)
                j+=1
            ls2 += '0'
            i+=1
    
        ## line 2 one's place
        i = 1
        while(i<(a+1)):
            ls2 += str(i)
            i+=1
        print(ls2)
