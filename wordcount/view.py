import operator

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def food(request):
    return HttpResponse("<h1>I am purely veg</h1>")

def about(request):
    return render(request,'about.html')

def count(request):
    text = request.GET['fulltext']
    text1 = text.split()

    worddict = {}

    for word in text1:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1


    return render(request,'count.html',{'text':text,'count':len(text1),'worddictionary':sorted(worddict.items(),key=operator.itemgetter(1),reverse = True)})