from django.shortcuts import render

# Create your views here.

finches = [
  {'name': 'Jasmine', 'breed': 'fatbrown', 'description': 'furry little demon', 'age': 3},
  {'name': 'Kat', 'breed': 'yellowtail', 'description': 'gentle and loving', 'age': 2},
]

def home(request):
    return render(request, 'home.html'),

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
