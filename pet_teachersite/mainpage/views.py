from django.http import HttpResponse
from django.urls import path
from django.shortcuts import redirect, render
from .forms import SignForm

def sign_up(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date = request.POST.get('date')
        if form.is_valid():
            return redirect(
                'https://wa.me/79614478065?text=Здравствуйте! ' + '\n'
                f'Меня зовут {first_name} {last_name}. Я бы хотел(а) '  + '\n'
                f'записаться на занятие на время {date}'
            )

    else:
        form = SignForm()
        return render(request, "mainpage/sign_up.html", {"form": form})