
#TODO:Implementing for all the sheets

import requests
from bs4 import BeautifulSoup
import PyPDF2
#Python Cheatsheets

py_url="https://thecodingworld.com/cheat-sheets/5/"
r_url="https://thecodingworld.com/cheat-sheets/6/"
css_url="https://thecodingworld.com/cheat-sheets/2/"
html_url="https://thecodingworld.com/cheat-sheets/"
java_url="https://thecodingworld.com/cheat-sheets/3/"
js_url="https://thecodingworld.com/cheat-sheets/4/"
and_url="https://thecodingworld.com/cheat-sheets/8/"
php_url="https://thecodingworld.com/cheat-sheets/7/"

print "Welcome to the cheat sheets world :D\n"
print "1) Python\n"
print "2) R\n"
print "3) HTML\n"
print "4) CSS\n"
print "5) Java\n"
print "6) Java Script"
print "7) PHP"
print "8) Andriod"

q=input("Enter the number  : ")

if(q==1):
    r=requests.get(r_url)
if(q==2):
    r=requests.get(r_url)
if(q==3):
    r=requests.get(html_url)
if(q==4):
    r=requests.get(css_url)
if(q==5):
    r=requests.get(java_url)
if(q==6):
    r=requests.get(js_url)
if(q==7):
    r=requests.get(php_url)
if(q==8):
    r=requests.get(and_url)

soup=BeautifulSoup(r.content,'html.parser')
temp=soup.findAll('a')
cheat_sheets=[]
merger=PyPDF2.PdfFileMerger()
links=[]
for i in temp:
    i=str(i)
    if ".pdf" in i:
        cheat_sheets.append(i)
        
cheat_sheets.pop(0)
for i in cheat_sheets:
    temp=i.split('href="')[1]
    temp=temp.split('">')[0]
    links.append(temp)
for i in links:
    r=requests.get(i)
    with open("temp.pdf",'w') as op:
        op.write(r.content)
    merger.append(PyPDF2.PdfFileReader('temp.pdf'),'r')
merger.write('Andr.pdf')

