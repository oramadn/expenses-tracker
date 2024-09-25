from django.http import HttpResponse

def index(request):
    return HttpResponse('We are at the index of recurrence')