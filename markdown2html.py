import re
def lista():
    return 0

def main():
    f=open("markdown_test.md","r+")
    f1=open("markdown_rules.txt","r+")
    mark_dict_comm={}
    pom=f1.readlines()
    slova="asdfghjklčćžmnbvcxyqwertzuiopšŽđYXCVBNMŽĆČLKJHGFDSAQWERTZUIOPŠĐ"
    for i in pom:
        mark, html=i.split(", ")
        mark_dict_comm[mark] = html[:-1]

    f1.close()
    tekst=f.readlines()
    html=""
    print(tekst)
    indikator_liste=False
    pocetak_liste=True
    for index, i in enumerate(tekst):
        if indikator_liste==False:
            if i == "\n":
                html+="<br>"
            if i[0] in mark_dict_comm.keys():
                mark, sadrzaj= i.split(" ",1)
                if mark in mark_dict_comm:
                    html+=mark_dict_comm[mark]+sadrzaj[:-1]+"</"+mark_dict_comm[mark][1:]
            elif i[0] in slova:
                html+="<p>"+i[:-1]+"</p>"
        elif i[0]==" ":
            print("ulazak")
            if re.search(" ^\d+",i):
                indikator_liste=True
                html+="<ol>"+"<li>"+i.strip()[2:]+"<ul>"
            if i[0:3]=="    " and i[index+1][0:3]!="    ":
                html+="<li>"+i.strip()+"<\li>"
            else:
                html+="</ul></li></ol>"





    print(html)
        
    f.close()
main()
