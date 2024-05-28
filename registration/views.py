# myapp/views.py
from django.shortcuts import render

from registration.models import Post

# display grid
# header and footer

def register(request):
    watches = Post.objects.all()
    context = {"title": "Swissmiller", "watches": watches}
    return render(request, "registration/register.html", context=context)
