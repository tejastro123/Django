from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    tejas = {'name':'Tejas', 'place':'Mars'}
    return render(request, 'index.html', tejas)
    #return HttpResponse("")
 
def about(request):
    return HttpResponse("about tejas <a href='/''>back</a>")

def yt(request):
    return HttpResponse('''<h1>Youtube link below<h1> 
                        <a href="https://www.youtube.com/">  Youtube</a>
                        <a href='/''>back</a>''')

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("remove punc <a href='/''>back</a>")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        param = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
             if char!="\n" and char!="\r":
                 analyzed=analyzed+char
        param = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        param = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        
    
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!='on'):
        return HttpResponse('ERROR')
    
    return render(request, 'analyze.html', param)

def ex1(request):
    s=''' Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br> <br> 
    <a href='/'>Home</a>'''
    return HttpResponse(s)

