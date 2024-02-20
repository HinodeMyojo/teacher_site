from django.http import HttpResponse, JsonResponse
from django.urls import path
from django.shortcuts import redirect, render
from .forms import SignForm

def sign_up(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            # Здесь мы просто передаем данные формы в контекст, отображаемый в модальном окне
            context = {'form': form, 'data': form.cleaned_data, 'show_modal': True}
            return render(request, 'mainpage/sign_up.html', context)

    else:
        form = SignForm()
        return render(request, "mainpage/sign_up.html", {"form": form})