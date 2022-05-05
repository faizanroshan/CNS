def bitStuffing(data):

    payload = ""
    count = 0
    for bit in data:

        if count == 5:

            payload = payload + "0"
            count = 0
        
        if bit == "1":

            count += 1
            payload += bit
        elif bit == "0":

            count = 0
            payload += bit 
    print(payload)

if __name__ == "__main__":

    data = "1011111100"
    bitStuffing(data)
