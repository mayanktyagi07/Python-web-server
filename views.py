from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey, this is Sttudent of UPES")