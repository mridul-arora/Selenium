from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys

#Simple page renders like this
def mainpage(request):
    return render(request,'index.html')

#When user clicks on the button
def output(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'index.html',{'data':data})

#Running an external python script
def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable,'C://Users//arora//Documents//Selenium//Whatsapp Automation//test//test.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'index.html',{'data1':out.stdout})
