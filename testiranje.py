import re
f=open("markdown_test.md","r+")
f1=open("markdown_rules.txt","r+")
mark_dict_comm={}
pom=f1.readlines()
slova="asdfghjklčćžmnbvcxyqwertzuiopšŽđYXCVBNMŽĆČLKJHGFDSAQWERTZUIOPŠĐ"
html=""
lista = f.readlines()
for index, i in enumerate(lista):
    if i[0]==" ":
        print(i)
        if re.search(" \d+",i):
            print("aha")
            html+="<ol>"+"<li>"+i.strip()[2:]+"<ul>"
            if i[0:3]=="    " and i[index+1][0:3]!="    ":
                html+="<li>"+i.strip()+"<\li>"
            else:
                html+="</ul></li></ol>"
