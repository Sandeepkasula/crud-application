from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import moodle
from .forms import moodleform
from django.http import HttpResponse

def index(request):
    shelf = moodle.objects.all()
    return render(request, 'create_view.html', {'shelf': shelf})

def upload(request):
    upload = moodleform()
    if request.method == 'POST':
        upload = moodleform(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form':upload})

def update_moodle(request, course_id):
    course_id = int(course_id)
    try:
        moodle_sel = moodle.objects.get(id = course_id)
    except moodle.DoesNotExist:
        return redirect('index')
    moodle_form = moodleform(request.POST or None, instance = moodle_sel)
    if moodle_form.is_valid():
       moodle_form.save()
       return redirect('index')
    return render(request, 'upload_form.html', {'upload_form':moodle_form})

def delete_moodle(request, course_id):
    course_id = int(course_id)
    try:
        moodle_sel = moodle.objects.get(id = course_id)
    except moodle.DoesNotExist:
        return redirect('index')
    moodle_sel.delete()
    return redirect('index')