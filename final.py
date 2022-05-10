import requests
import json
def function():
    response=requests.get("http://saral.navgurukul.org/api/courses")
    with open("co.json","w") as f : 
        cource=json.loads(response.text)
        json.dump(cource,f,indent=4)
    with open("co.json","r") as f : 
        var=json.load(f)
    i=0
    id=[]
    while i<len(cource["availableCourses"]):
        name=cource["availableCourses"][i]["name"]
        id1=cource["availableCourses"][i]["id"]
        id.append(id1)
        print(i,"",name,id1)
        i+=1
    User=int(input("enter your serial number: "))
    var2=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[User])+"/exercises")
    a=var2.json()
    j=0
    l=0
    slug=[]
    while j<len(a["data"]):
        print(l,a["data"][j]["name"])
        slug.append(a["data"][j]["slug"])
        j+=1
        l+=1
    User1=int(input("enter your slug number: "))
    var3=requests.get("http://saral.navgurukul.org/api/courses/"+str(User)+"/exercise/getBySlug?slug="+slug[User1])
    b=var3.json()
    print(b["content"])
    p=0
    while p<len(slug):
        User2=input("enter up: ")
        if User2=="up" or User2=="UP":
            var4=requests.get("http://saral.navgurukul.org/api/courses/"+str(User)+"/exercise/getBySlug?slug="+slug[User1-1])
            e=var4.json()
            print(e["content"])
        elif User2=="previous" or User2=="Previous":
            var4=requests.get("http://saral.navgurukul.org/api/courses/"+str(User)+"/exercise/getBySlug?slug="+slug[User1])
            f=var4.json()
            print(f["content"])
        elif User2=="Next" or User2=="next":
            var4=requests.get("http://saral.navgurukul.org/api/courses/"+str(User)+"/exercise/getBySlug?slug="+slug[User1+1])
            g=var4.json()
            print(g["content"])
        User3=input("enter again or exit")
        if User3=="again" or User=="AGAIN":
             function()
    
        else:
            break
        p+=1
function()