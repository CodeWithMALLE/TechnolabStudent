from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, "main/index.html", {})


def candidater(request):
	return render(request, "main/candidature.html", {})
