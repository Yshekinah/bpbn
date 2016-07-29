from django.shortcuts import render


def checkAdmin(request):
    if request.user.groups.exclude(name='Admin').exists():
        return render(request, 'domainmanager/index.html')
