from django.shortcuts import render, redirect
# from datetime import datetime
from .models import Post
from .forms import MyForm

# Create your views here.
def home (request):

    posts = Post.objects.all()
    # date = datetime.now().date

    return render(request, 'pages/index.html',{
        # 'date': date,
        'posts': posts,
    })

def form(request):
    if request.method == 'POST':
        enter = MyForm(request.POST)
        if enter.is_valid():
            enter.save()
            return redirect('home')
    else:
        enter = MyForm()
    
    return render(request, 'pages/form.html', {
        'enter': enter
    })