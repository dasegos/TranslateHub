from django.views import View
from django.shortcuts import render


def about(request):
    return render(request, 'translations/about.html', {})


def main(request):
    return render(request, 'translations/main.html', {})


def original_texts(request):
    return render(request, 'translations/original_texts_list.html', {})


def translations(request):
    return render(request, 'translations/translations_list.html', {})


class OriginalTextView(View):
    template_view = 'translations/original_text.html'

    def get(self, request):
        ...

    def post(self, request):
        ...


class TranslationView(View):
    template_view = 'translations/translation.html'

    def get(self, request):
        ...

    def post(self, request):
        ...


class TranslateView(View):
    template_view = 'translations/translate.html'

    def get(self, request):
        ...

    def post(self, request):
        ...
 