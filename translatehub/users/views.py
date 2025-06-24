from django.views import View
from django.shortcuts import render


def about(request):
    return render(request, 'translations/about.html', {})


def main(request):
    return render(request, 'translations/about.html', {})


class MyProfileView(View):
    template_view = 'users/my_profile.html'

    def get(self, request):
        ...

    def post(self, request):
        ...
