# myapp/views.py
from django.shortcuts import render

from registration.models import Watch

# display grid
# header and footer

def register(request):
    if request.method == "GET":
        searched_text = request.GET.get("searched_text")
        if searched_text:
            watches = Watch.objects.filter(title__contains=searched_text)
        else:
            watches = Watch.objects.all()
    # print(watches[0].brand.description)
    context = {"title": "Swissmiller", "watches": watches}
    return render(request, "registration/register.html", context=context)

