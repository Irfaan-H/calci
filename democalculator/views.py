from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.


def index(request):
    return render(request,"index.html")
def reset(request):
   
    return render(request,"index.html",{'result':""})

def calculator(request):
    receivedinput = request.POST['calci']

    if receivedinput =="":
        return render(request,"index.html",{'result':""})

    fvalue=re.findall(r"(\d+)",receivedinput)

    voperator =['+','-','*','/','.','%']

    foperator =[]



    for ri in receivedinput:


        for vo in voperator:
            if ri == vo:
                foperator.append(vo)

                re.findall(r"(\d+)",receivedinput)

    for fo in foperator:
        if fo=='.':
            i=foperator.index(fo)
            result1 =fvalue[i] +'.'
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i] =result1

    for fo in foperator:
        if fo=='%':
            i= foperator.index(fo)
            result1 = float(fvalue[i]) * float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i] = str(result1)

    for fo in foperator:
        if fo=='-':
            i=foperator.index(fo)
            result1 =float(fvalue[i])-float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i]=str(result1)
    
    for fo in foperator:
        if fo=='/'   :
            i=foperator.index(fo)
            result1 = float(fvalue[i])/ float(fvalue[i+1])
            foperator.remove(foperator[i])   
            fvalue.remove(fvalue[i+1])
            fvalue[i]=str(result1)


    for fo in foperator:
        if fo =='*':
            i= foperator.index(fo)
            result1 =float(fvalue[i]) * float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i]=str(result1)

    for fo in foperator:
        if fo=='+':
            i = foperator.index(fo)
            result1 =float(fvalue[i]) +float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i]=str(result1)
           


    if len(foperator) !=0:
        
        if foperator[0]=='/':
            result2 = float(fvalue[0]) / float(fvalue[1])

        elif foperator[0]=='*':
            result2 = float(fvalue[0]) * float(fvalue[1])

        elif foperator[0]=='+':
            result2 = float(fvalue[0]) + float(fvalue[1]) 
        else:
            result2 = float(fvalue[0]) - float(fvalue[1])
    else:
        result2 = float(fvalue[0])

        result =round(result2,2)
        responce= render(request,"index.html",{'result':result})
        return responce

    
