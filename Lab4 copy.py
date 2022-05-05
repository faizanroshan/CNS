def getParityBit(data):

    count = 0
    for bit in data:

        if bit == "1":
            count += 1
    
    if count % 2  == 0:
        return 1
    else:
        return 0

if __name__ == "__main__":

    size = int(input("Enter size of dataframe:"))
    data = input("Enter dataframe:")

    parityBit = getParityBit(data)
    print("Parity bit is", parityBit)