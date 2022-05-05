def checkCRC(dividend, divisor):

    size = len(divisor)
    dividend += ("0" * (size-1))
    print(dividend)
    divisor_num = int(divisor, 2)
    quotient = ""
    current = dividend[0:size] # current 
    for index in range(size, len(dividend)):

        if index > size: # adding next digit to current dividend from given dividend
            current = current + dividend[index]

        current_num = int(current, 2) # store the current number in decimal system
        
        if(int(current, 2) >= int(divisor, 2)) : # if current number is greater than divisor xor with divisor

            
            current_num = current_num ^ divisor_num
            quotient += "1"
            print(current, "xor", divisor, "Q", quotient)
            current = bin(current_num).replace("0b", "")
             
        else: # if current number is smaller than divisor xor with zeros

            current_num = current_num ^ int(("0" * size), 2)
            quotient += "0";
            print("else", current, "xor", ("0" * size), "Q", quotient)
            current = bin(current_num).replace("0b", "") # size of divisor
            quotient += "1"

if __name__ == "__main__":

    # size_dividend = int(input("Enter size of dataframe:"))
    # dividend = input("Enter dividend dataframe:")

    # size_divisor = int(input("Enter size of divisor dataframe:"))
    # divisor = input("Enter divisor dataframe:")

    dividend = "1101011111"
    divisor = "10011"
    checkCRC(dividend, divisor)

