from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('giriş başarılı')
            return redirect('addTransfer')
        else:
            print('kullanıcı adı veya paralo yanlış')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if repassword == repassword:
            if User.objects.filter(username = username).exists():
                print('bu kullanıcı adı alınmış.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('bu email alınmış.')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    print('kullanıcı oluşturuldu.')
                    return redirect('login')
        else:
            print('parolalar eşleşmiyor')
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    return render(request, 'user/logout.html')
