with open('new.txt',"r") as file:
    lines = [line.strip() for line in file]
    new_gmail = open("gm1.txt","w",)   
    new_yahoo = open("ym1.txt","w",)
    new_hotmail  = open("hm1.txt","w",)
    other = open("other.txt","w")

    
    for line in lines:
        if (line.split("@")[1])=="gmail.com":
           new_gmail.write(line +"\n")
        elif (line.split("@")[1])=="yahoo.com":
            new_yahoo.write(line +"\n")
        elif (line.split("@")[1])=="hotmail.com":
            new_hotmail.write(line +"\n")
        else:
            other.write(line + "\n") 
