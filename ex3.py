
def testList(  inputlist):

    def isListOfInts(listint):
        return all(isinstance(element, int) for element in listint)
    
    try:
        if isinstance(inputlist, list):
            a = isListOfInts(inputlist)
            print(str(inputlist) + ' --> ' + str(a))
        else:
            raise ValueError(str(inputlist) + ' - arg not of <list> type')

    except ValueError as error:
        print(repr(error))   
