dle = "DLE" # DLE (data link escape)
stx = "STX" # STX (start of text)
etx = "ETX" # etx (end of text)

dle_ascii = ord('*')
stx_ascii = ord('#')
etx_ascii = ord('$')
def sent_data(data):

    global dle, stx, etx, dle_ascii
    if data == "":

        return None
    else:

        sent_data = ""
        
        # intially add DLE and STX to the start of the frame
        sent_data += dle + stx
        
        if ord(data[0]) != dle_ascii:

            sent_data += data[0] # add first character
            sent_data += dle + dle
        else:

            sent_data += dle + dle

        for char in data[1:]:

            char_ascii = ord(char)
            if char_ascii != dle_ascii:

                sent_data += char
            else:

                sent_data += dle + dle
        
        sent_data += dle + etx # frame ends with DLE and ETX
        
    return sent_data

def receiver_data(sender_data):

    decoded = ""
    decoded += sender_data[6] # extract first character seperately

    index = 13
    while index < len(sender_data):

        if sender_data[index: index+3] == "DLE" and sender_data[index+3: index+6] == "DLE":

            decoded += chr(dle_ascii)
            index += 6

        elif sender_data[index: index+3] == "DLE" or sender_data[index: index+3] == "ETX":

            index += 3 
        else:
            decoded += sender_data[index]
            index += 1

    return(decoded)

if __name__ == "__main__":

    data = 'rg*m'
    sender_data = sent_data(data)
    print("Sender data:", sender_data)
    received_data = receiver_data(sender_data)
    print("Receiver data:", received_data)