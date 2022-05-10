ayu=[5,2,[10,20]]
list1=[]
i=0
var=1
var2=1
while i<len(ayu):
    if type(ayu[i])==int:
        var2=var2*ayu[i]
    elif type(ayu[i])==list:
        j=0
        while j<len(ayu[i]):
            var=var*ayu[i][j]
            j+=1
    i+=1
list1.append(var2)
list1.append(var)
print(list1)