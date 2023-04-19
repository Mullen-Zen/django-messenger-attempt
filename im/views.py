from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.
def detail(request, user_id):
    question = get_object_or_404(User, pk=user_id)
    return render(request, "polls/detail.html", {"question": question})