from django.middleware.csrf import get_token

from .forms import CustomSignUpForm,  UpdateUserForm
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,  logout
from django.shortcuts import redirect
from datetime import datetime
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetDoneView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

import re
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import string
# users/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import UserProfile

from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Reception



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)

def register(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')
        else:
            # Handle form errors
            print(form.errors)
    else:
        form = CustomSignUpForm()

    return render(request, 'users/signup.html', {'form': form})

from django.contrib.auth.decorators import login_required

def user_profile(request):
    user = request.user
    receptions = Reception.objects.filter(patient_name=user, comed=False, declined=False, no_show=False)
    upcoming_reception = receptions.filter(date__gte=datetime.now()).first()  # Получение ближайшего будущего приема

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)


        print(request.POST)  # Вывести все переданные данные для проверки
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Ваш личный кабинет успешно обновлён')
            return redirect('users:user_profile')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
            print(user_form.errors)  # Вывод ошибок в консоль
    else:
        user_form = UpdateUserForm(instance=user)


    context = {
        'user': user,
        'receptions': receptions,
        'upcoming_reception': upcoming_reception,
        'user_form': user_form,
    }

    return render(request, 'users/user_profile.html', context)


# accounts/views.py


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:user_profile')  # Redirect to the user's profile page after login
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the home page or any other desired page after logout


def get_user_info_by_email(request, email):
    try:
        user = get_object_or_404(UserProfile, email=email)
        user_data = {
            'username': user.username,
            'full_name': user.full_name,
            'address': user.address,
            'phone': user.phone,
            'date_of_birth': user.date_of_birth,
            'bio': user.bio,
            # Add other fields as needed
        }
        return JsonResponse(user_data)
    except Http404:
        return JsonResponse({'error': 'User not found'}, status=404)



def csrf_token_endpoint(request):
 # Use Django's get_token function to obtain the CSRF token
 csrf_token = get_token(request)
 return JsonResponse({'csrftoken': csrf_token})



@login_required
def my_receptions(request):
    return render(request, 'users/my_receptions.html', {'reception': Reception})


from django.contrib.auth.views import PasswordResetView

class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/registration/password_reset_form.html'
    email_template_name = 'users/registration/password_reset_email.html'
    subject_template_name = 'users/registration/password_reset_subject.txt'
    success_url = reverse_lazy('users:password_reset_done')

class CustomPasswordResetDone(PasswordResetDoneView):
    template_name = 'users/registration/password_reset_done.html'

from django.contrib.auth.views import PasswordResetConfirmView

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/registration/password_reset_confirm.html'


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/registration/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users:login')


User = get_user_model()

class RecoverAccount(APIView):
    def post(self, request, *args, **kwargs):
        contact = request.data.get('contact')
        user = None

        if re.match(r'^\+\d{10,15}$', contact):  # Проверка телефона
            user = User.objects.filter(phone=contact).first()
        elif re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', contact):  # Проверка email
            user = User.objects.filter(email=contact).first()

        if user:
            reset_token = get_random_string(30)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            send_mail(
                'Восстановление доступа',
                f'Перейдите по ссылке для сброса пароля: {reset_url}',
                'muk888@mail.ru',
                [user.email],
                fail_silently=False,
            )

            return Response({"message": "Инструкции отправлены."}, status=status.HTTP_200_OK)
        return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

User = get_user_model()
class SendTempPassword(APIView):
    def post(self, request, *args, **kwargs):
        contact = request.data.get('contact')
        user = None

        if re.match(r'^\+\d{10,15}$', contact):
            user = User.objects.filter(phone=contact).first()
        elif re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', contact):
            user = User.objects.filter(email=contact).first()

        if user:
            first_char = get_random_string(1, string.ascii_uppercase)
            characters = string.ascii_letters + string.digits + "!@#$%^&*()"
            temp_password = first_char + get_random_string(7, characters)
            user.set_password(temp_password)
            user.save()

            return Response({"temp_password": temp_password}, status=status.HTTP_200_OK)

        return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

