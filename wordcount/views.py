# this will return back the HTTP Request
from django.http import HttpResponse
from django.shortcuts import render
import operator


# this is the HOME page the user will get
def homepage(request):
    return render(request, 'home.html')

# About web page
def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordList = fulltext.split()

    worddictionary = {}

    for word in wordList:
        if word in worddictionary:
            # Increases
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1
    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordList), 'worddictionary':sortedWords})
