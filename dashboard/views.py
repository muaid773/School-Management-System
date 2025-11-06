from django.shortcuts import render

# Create your views here.
def main_dashboard(request):
    return render(request, 'dashboard_page.html')