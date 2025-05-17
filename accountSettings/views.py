from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserSettingsForm
from .models import UserSettings
from django.contrib.auth.decorators import login_required

def index (request):
    return HttpResponse('index page')

def runSettings (request):
    template = loader.get_template('Reader_Settings.html')
    return HttpResponse (template.render())

def about (request):
    return HttpResponse('about page')

@login_required
def settings_view(request):
    try:
        user_settings = UserSettings.objects.get(user=request.user)
    except UserSettings.DoesNotExist:
        user_settings = UserSettings(user=request.user)

    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=user_settings)
        if form.is_valid():
            form.save()
            return redirect('settings')  # Redirect to the same page or anywhere you want
    else:
        form = UserSettingsForm(instance=user_settings)

    return render(request, 'accountSettings.html', {'form':form})