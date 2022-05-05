def testCase1(string):

    count = 0
    for i in string:
        
        count += 1

    return count

def testCase2(string):

    count = 0
    for i in string:

        if i != ' ':
            count += 1
    return count 

def testCase3(string):

    string_1 = ''
    for i in string:

        if i == ' ':

            string_1 += '*'
        else:
            string_1 += i
    
    return string_1

def testCase4(string):

    string_1 = ''
    count = 0
    for i in string:
    
        count += 1
        if count == 5:
            count = 0
            string_1 += '*'
        else:
            string_1 += i
    return string_1

if __name__ == "__main__":

    string = "this is CN Lab"
    
    print(testCase1(string))
    print(testCase2(string))
    print(testCase3(string))
    print(testCase4(string))