from django.shortcuts import render, redirect
from django.conf import settings
from config import asset_storage

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Files

@login_required

def file_list(request):
    files = Files.objects.all()[:10]
    return render(request, 'input/file_list.html', {'files':files})

from django.views.generic.edit import CreateView

class FileUploadView(LoginRequiredMixin,  CreateView):
    model = Files
    fields = ['file', 'text']
    template_name = 'input/upload.html'


    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/loading')
        else:
            return self.render_to_response({'form':form})