from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from django.shortcuts import redirect


def home(request):
    return render(request, 'app/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        adharcard = request.POST.get('adharcard')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        # hashed_password = make_password(password)

        user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            address=address,
            adharcard=adharcard,
            phone=phone,
            age=age
        )
        user.save()
        return redirect('app/login.html')
    return render(request, 'app/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'app/login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(email=email)
            # print(email)
        except CustomUser.DoesNotExist:
            return render(request, 'app/login.html')

        if user.password==password:
            request.session['user_email'] = email
            return redirect('dashboard')


def dashboard(request):
    email = request.session.get('user_email')
    context = {'email': email}
    return render(request, 'app/main.html', context)



