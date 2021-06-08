from settings.models import Settings



def myfooter(request):
    myfooter = Settings.objects.last()
    return {'myfooter': myfooter}