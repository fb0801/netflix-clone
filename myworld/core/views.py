from django.shortcuts import render
from django.views import View
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request, 'profileList.html',{
            'profiles':profiles         
                      })