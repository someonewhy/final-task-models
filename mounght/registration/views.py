from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .forms import RegistrationForm
from .models import RegistrationCode
from django.http import HttpResponse
from django.contrib.auth import logout

@login_required
def registration(request):
    if request.user.is_authenticated:
        return HttpResponse("Вы уже зарегистрированы.")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Генерация и сохранение одноразового кода регистрации
            code = get_random_string(length=20)
            registration_code = RegistrationCode(user=user, code=code)
            registration_code.save()

            # Отправка кода на почту
            send_mail(
                'Регистрация на сайте',
                f'Ваш одноразовый код для регистрации: {code}',
                'noreply@example.com',
                [user.email],
                fail_silently=False,
            )

            return redirect('registration:registration_success')
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration_form.html', {'form': form})

@login_required
def registration_success(request):
    return render(request, 'registration/registration_success.html')

def logout_view(request):
    logout(request)
    return redirect('registration:logout_success')