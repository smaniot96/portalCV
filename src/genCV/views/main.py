
from django.shortcuts import render
from genCV.forms import CVGeneratorForm
from genCV.services.cvGenerator import generate_cv_or_cover_letter

def cv_form_view(request):
    result = None
    if request.method == 'POST':
        form = CVGeneratorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result = generate_cv_or_cover_letter(
                name=cd['name'],
                job_title=cd['job_title'],
                experience=cd['experience'],
                job_description=cd['job_description'],
                generate_type=cd['generate_type'],
            )
    else:
        form = CVGeneratorForm()
    
    return render(request, 'genCV/generateCV.html', {'form': form, 'result': result})
