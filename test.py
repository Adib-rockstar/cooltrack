from collections import Counter
data=[]
value=""
time_data=int(input(""))
for i in range(time_data):
    num_data=int(input(""))
    for j in range(num_data):
        text=input("Name:")
        first_word = text.split()[0]
        data.append(first_word)
    coun=Counter(data)
    lis=list(coun.items())
    x=len(lis)
    max=lis[0][1]
    for i in range(0,x):
        if (lis[i][1] > max):
            max=lis[i][1]
    for i in range(0,x):
        if(lis[i][1]==max):
            value=value  + str(lis[i][0])+ " " + str(max)  + "1" 
    data=[]    
print(value.replace("1",'\n'))

