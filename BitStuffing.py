def bitStuffing(data):

    payload = ""
    count = 0

    for bit in data:
        
        print(payload, count)
        if bit == "1" and count == 4:

            count = 0
            payload = payload + bit + "0"

        elif bit == "0":
            
            count = 0
            payload = payload + bit
        elif bit == "1":

            count += 1
            payload = payload + bit

        
    
    print("data to be transferred: ", payload)

if __name__ == "__main__":

    data = "10111101100"
    #input("Enter the data: ")
    bitStuffing(data)