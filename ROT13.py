#solve ROT13 for alphabet 


decode= input('enter your encode value: \n') #enter your data
entry= "abcdefghijklmnopqrstuvwxyz" 
b= 13 #shift +13
new=len(decode) 
output=""
for item in range(new):
    c=decode[item]
    find=entry.find(c)
    rot=(find + b)%26
    output += entry[rot]
print(output)