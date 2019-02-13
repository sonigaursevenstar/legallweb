from legaldoc.models import Headerfooter
def categories(request):
    return {
        'categories': Headerfooter.objects.all()
    }
