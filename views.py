#this is file made for testing
#we are going to create pipelines in django
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    mytext = request.GET.get('text', 'off')
    mycheckbox = request.GET.get('mycheckbox','default')
    upbox = request.GET.get('upbox', 'off')
    capbox = request.GET.get('capbox', 'off')
    charbox = request.GET.get('charbox', 'off')
    punctuations= '''(){}'\/&@#$%*!^[]-_<>'''
    analyzed = ""
    if mycheckbox == "on":
            for char in mytext:
                if char not in punctuations:
                    analyzed = analyzed+char
            params = {'purpose': "after removing punctuation", 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
    elif upbox == "on":
            for char in mytext:
                    analyzed = analyzed+char.upper()
            params = {'purpose': "Converted to UpperCase", 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
    elif capbox == "on":
            for char in mytext:
                    analyzed = analyzed+char.capitalize()
            params = {'purpose': "Capitalized text is ", 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
    elif charbox == "on":
            for char in mytext:
                    analyzed = analyzed+char
                    totalcount = len(analyzed)
            params = {'purpose': "total number of characters", 'analyzed_text': totalcount}
            return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error no checkbox selected")



