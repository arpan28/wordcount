from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'hello':"liverpool fc"})

def count(request):
    full_text = request.GET["fulltext"]
    count = full_text.split()
    countDict = {}
    for words in count:
        if words not in countDict.keys():
           countDict[words] = 1
        else:
            countDict[words] += 1
    return render(request,'count.html',{"fulltext":full_text,"count":len(count),"wordcount":countDict.items()})

def about(request):
    return render(request,'about.html')
