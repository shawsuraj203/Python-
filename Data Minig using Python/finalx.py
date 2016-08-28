import urllib
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
dict={}
rl = "http://www.carwale.com/newcars/search_result.aspx?bs=1&pn=1"
tml = urllib.request.urlopen(rl).read()
oup = BeautifulSoup(tml)
fd=open("diesel.txt",'w',encoding='utf-8');
fp=open("petrol.txt",'w',encoding='utf-8');
def s(soups):
    for soup in soups.findAll("div",{"style":"margin-top: 20px;"}):
        for pous in soup.findAll("p",{"class":"text-grey","style":"margin-top: 3px;"}):
            for script in pous("a",{"class":"f-small"}):
                script.extract()
        for link in soup.findAll("a",href=True,text="read complete review"):
            html2=urllib.request.urlopen("http://www.carwale.com"+link["href"]).read()
            soup2 = BeautifulSoup(html2)
            for soup3 in soup2.findAll("div",{"class":"mid-box margin-top20"}):
                for soupx in soup3.findAll("table",{"width":"100%"}):
                    if (soupx(text=re.compile('Version Reviewed')))==[]:
                        pass
                    else:
                        for soupy in soupx.findAll("td",{"width":None}):
                            if soupy.get_text() in dict.keys():
                                if dict[soupy.get_text()]=="Diesel":
                                    print(pous.get_text())
                                    fd.write(pous.get_text())
                                    for sou3 in soup2.findAll("div",{"class":"mid-box margin-top20"}):
                                        for soux in sou3.findAll("table",{"width":"100%"}):
                                            print(soux.get_text())
                                            fd.write(soux.get_text())
                                        for sou4 in sou3.findAll("h3",{"class":"font14"}): 
                                            sou5=sou4.parent
                                            print(sou5.get_text())
                                            fd.write(sou5.get_text())
                                else:
                                    print(pous.get_text())
                                    fp.write(pous.get_text())
                                    for sou3 in soup2.findAll("div",{"class":"mid-box margin-top20"}):
                                        for soux in sou3.findAll("table",{"width":"100%"}):
                                            print(soux.get_text())
                                            fp.write(soux.get_text())
                                        for sou4 in sou3.findAll("h3",{"class":"font14"}): 
                                            sou5=sou4.parent
                                            print(sou5.get_text())
                                            fp.write(sou5.get_text())
    for links in soups.findAll("a",href=True,text="Next"):
        html=urllib.request.urlopen("http://www.carwale.com"+links["href"]).read()
        soups = BeautifulSoup(html)
        s(soups)
def st(oup):
    for oup1 in oup.findAll("td",{"class":"ver-pdd"}):
        for oup3 in oup1.findAll("a"):
            pass
        for oup2 in oup1.findAll("span",{"class":"text-grey"}):
            if (oup2(text=re.compile('Diesel')))==[]:
                dict[oup3.get_text()]='Petrol'
            else:
                dict[oup3.get_text()]='Diesel'
    for oup1 in oup.findAll("tr",{"class":"model-row version-row"}):
        for oup3 in oup1.findAll("a",{"class":"href-grey"}):
            tml=urllib.request.urlopen("http://www.carwale.com"+oup3["href"]).read()
            oup1 = BeautifulSoup(tml)
            s(oup1)
    for ink in oup.findAll("a",href=True,text="Next"):
        tml=urllib.request.urlopen("http://www.carwale.com"+ink["href"]).read()
        oup = BeautifulSoup(tml)
        dict.clear()
        st(oup)
        break
st(oup)
#write
#your
#code
#file
#and
#re
#code
#here
#and
#dont
#touch
#my
#code
fp.close()
fd.close()
