file1=open("LogoArt.txt","r")
file2=open("LogoRLE.txt","r")
n = -1
m = -1
g = 6
k = "0"
List3 = []
myList = []
myList2 = []

def ReadFromFile(file2):
     file2=open("LogoRLE.txt","r") #w =write, r =read, a=append
     Data = file2.readlines()# We can now read a string of data
     for lines in Data:
            line = lines.strip()
            myList.append(str(line))
     file2.close() #Before we close it at the end.
     return Data

def ReadFromFile2(file1):
     file1=open("LogoArt.txt","r")
     Data = file1.readlines()# We can now read a string of data
     for lines in Data:
            line = lines.strip()
            myList2.append(str(line))
     file1.close() #Before we close it at the end.
     return Data

def rle_decode(data):
    decode = ''
    count = ''
    k ="0"
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
                 
    return decode

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if (int(count) / 10) < 1:
                 count = str(k) + str(count) 
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        if (int(count) / 10) < 1:
             count = str(k) + str(count)
        encoding += str(count) + prev_char
        return encoding
      
def print_menu():       ## Your menu design here
    print (30 * '-')
    print ("   MENU")
    print (30 * '-')
    print ("1. Enter RLE")
    print ("2. Display ASCII art")
    print ("3. Convert to ASCII art")
    print ("4. Convert to RLE")
    print ("5. Quit")
    print (30 * '-')

loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = int(input("Enter your choice [1-5]: "))
     
    if choice==1:     
        print ("Menu 1 has been selected")
        z = input("How many lines of ASCII do you want?")
        for count in range(0,int(z)):
             j = input("Enter ASCII: ")
             List3.append(j)
        n = -1
        for count in range(0,len(List3)):
             n = n + 1
             decoded_val = rle_decode(List3[n])
             print(decoded_val)
        List3.clear()
    elif choice==2:
        print ("Menu 2 has been selected")
        k = input("Input path of text file: ")
        f = open(k)
        print(f.read())   
    elif choice==3:
        n = -1
        print ("Menu 3 has been selected")
        ReadFromFile(file2)
        for count in range(0,len(myList)):
             n = n + 1
             decoded_val = rle_decode(myList[n])
             print(decoded_val)
        myList.clear()
    elif choice==4:
        n = -1
        print ("Menu 4 has been selected")
        ReadFromFile2(file1)
        for count in range(0,len(myList2)):
             n = n + 1
             encoded_val = rle_encode(myList2[n])       
             print(encoded_val)
        myList2.clear()
    elif choice==5:
        print ("Menu 5 has been selected")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        input("Wrong option selection. Enter any key to try again..")
