from django.shortcuts import render

# Create your views here.


def custom_error_404_view_here(request, exception=None):
	print(request.user)
	return render(request, '404.html')
def custom_error_500_view_here(request, exception=None):
	return render(request, '404.html')
def custom_error_403_view_here(request, exception=None):
	return render(request, '404.html')