from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import ReviewModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        
        try:
            User.objects.create_user(username_data, '', password_data)

        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})
    else:
        #print(User.objects.all())
        return render(request, "signup.html", {})
    
    return render(request, "signup.html", {})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')#list がエラーになる、not found

        else:
            return redirect('login')
    return render(request, 'login.html')

def listview(request):
    object_list = ReviewModel.objects.all()
    return render(request, 'list.html', { 'object_list':object_list})

def detailview(request, pk):
    object = ReviewModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

class CreateClass(CreateView):
    template_name = 'create.html'
    model = ReviewModel
    fields = ('title', 'content', 'author', 'images', 'evaluation')
    success_url = reverse_lazy('list')


"""
signup.htmlが入っているディレクトリをDjangoに伝えるため、settings.pyでDIRSを設定しないといけない
DIRSでは任意の場所・名前でテンプレートディレクトリーを追加できる
from django.http import HttpResponse
def hello(request) :
    responseobject = HttpResponse('<p>hello world</p>')
    return responseobject
"""