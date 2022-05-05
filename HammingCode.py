'''
implement a python program to detect error bit position and correcting the bit value in a given data frame
'''
def getParityBit(data):

    count = 0
    for bit in data:
        
        if bit == '1':
            count += 1
    
    if count % 2 == 0:

        return '0'
    else:
        return '1'

def getHammingCode(arr, data):

    # assign data bit d7, d6, d5, d3
    arr[7], arr[6], arr[5], arr[3]  = data[0], data[1], data[2], data[3]
    # calculate parity
    arr[1] = getParityBit(arr[3]+arr[5]+arr[7]) #p1 = d3 d5 d7
    arr[2] = getParityBit(arr[3]+arr[6]+arr[7]) #p2 = d3 d6 d7
    arr[4] = getParityBit(arr[5]+arr[6]+arr[7]) #p4 = d5 d6 d7

    return arr[::-1]

def getErrorPosition(arr):

    p_1 = getParityBit(arr[7] + arr[5] + arr[3] + arr[1])
    p_2 = getParityBit(arr[6] + arr[5] + arr[2] + arr[1])
    p_4 = getParityBit(arr[4] + arr[3] + arr[2] + arr[1])
    print(str(p_4)+str(p_2)+str(p_1))
    return int(str(p_4)+str(p_2)+str(p_1), 2)

if __name__ == "__main__":

    # let the dataframe size be 7 bit
    # 2^r >= m+r+1

    arr = ['0' for _ in range(8)]
    data = "1011" #strictly 4 digit

    hammingCode = getHammingCode(arr, data)
    print(hammingCode[:-1])
    error_position = getErrorPosition(hammingCode)
    print(error_position)