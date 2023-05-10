from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView


def index(request):
    return render(request, "index.html", {})
