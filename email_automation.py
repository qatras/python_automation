


with open("file.txt",'r') as file:     #type your txt filename instead of file1.txt
    lines = [line.strip() for line in file]

with open("gm.txt",'w') as file: #new txt file will be 'gm.txt' for gmail
    for line in lines:
        if (line.split("@")[1])=="gmail.com":
            file.write(line + " \n")
            #file.write(line + ",-by su-\n") for add more words

with open("ym.txt",'w') as file: #new txt file will be "ym.txt" for yahoo
    for line in lines:
        if (line.split("@")[1])=="yahoo.com":
            file.write(line + "\n")    
with open("hm.txt",'w') as file:  #new txt file will be "hm.txt" for hotmail
    for line in lines:
        if (line.split("@")[1])=="hotmail.com":
            file.write(line + "\n")                