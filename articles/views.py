from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcom to Denver Law Review's website.</h1>")
