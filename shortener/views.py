from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import URL

def shorten_url(request):
    shortened_url = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            custom_alias = form.cleaned_data.get('custom_alias')
            if custom_alias:
                if URL.objects.filter(shortened_url=custom_alias).exists():
                    form.add_error('custom_alias', 'This alias is already taken')
                else:
                    url_instance = form.save(commit=False)
                    url_instance.shortened_url = custom_alias
                    url_instance.save()
                    shortened_url = url_instance.shortened_url
            else:
                url_instance = form.save()
                shortened_url = url_instance.shortened_url
    else:
        form = URLForm()
    return render(request, 'home.html', {'form': form, 'shortened_url': shortened_url})

def redirect_url(request, shortened_url):
    url_instance = get_object_or_404(URL, shortened_url=shortened_url)
    return redirect(url_instance.original_url)
