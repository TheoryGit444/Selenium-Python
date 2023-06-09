""" write a program to read the file.
search for the keyword "Infosys DOG", if string is found, copy that line to the other new file."""


file_reader=open("InfosyDOG.txt","r")

list=file_reader.readlines()



list1=[]

search_string="infosys dog"

#find string in file and spilt and save it in list.

for x in list:
    
    y=x.lower().find(search_string)
    
    if(y>=0):
        list1.append(x)
    
print(list1)   

#copy the content of list in file
file_writer=open("Finalfile.txt","a")

for x in list1:
    file_writer.write(x)

file_reader.close()    

file_writer.close()

# Yipeeee I win
