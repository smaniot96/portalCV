
from django.shortcuts import render
from django.http import FileResponse
import tempfile
from genCV.forms import CVGeneratorForm
from genCV.services.cvGenerator import generate_cv
import subprocess
import tempfile
import os
from django.http import HttpResponse

import subprocess
import tempfile

def latex_to_pdf(latex_code: str) -> bytes:
    with tempfile.TemporaryDirectory() as tmpdir:
        tex_file = f"{tmpdir}/doc.tex"
        pdf_file = f"{tmpdir}/doc.pdf"
        with open(tex_file, "w") as f:
            f.write(latex_code)
        # Compile
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file],
            cwd=tmpdir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode != 0:
            raise RuntimeError(f"LaTeX compilation failed:\n{result.stdout.decode()}\n{result.stderr.decode()}")
        with open(pdf_file, "rb") as f:
            pdf_bytes = f.read()
        return pdf_bytes




def cv_form_view(request):
    context = None

    if request.method == 'POST':
        form = CVGeneratorForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            data = form.cleaned_data  # Django automatically returns a dict
            result = generate_cv(data)  # Just pass it directly
            pdf_bytes = latex_to_pdf(result)
            tmp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            tmp_pdf.write(pdf_bytes)
            tmp_pdf.flush()
            tmp_pdf_name = tmp_pdf.name
            pdf_filename = os.path.basename(tmp_pdf_name)

            tmp_pdf.close()
            context = {
                "form": form,
                "result": result,
                "pdf_temp_path": tmp_pdf_name,
                "pdf_filename": pdf_filename,  # full path on server
                    }
    else:
        form = CVGeneratorForm()
    
    return render(request, 'genCV/generateCV.html',  context)



def serve_temp_pdf(request, filename):
    temp_path = os.path.join("/tmp", filename)
    if os.path.exists(temp_path):
        return FileResponse(
            open(temp_path, "rb"),
            content_type="application/pdf",
            headers={"Content-Disposition": f"inline; filename={filename}"}
        )
    return HttpResponse("PDF not found.", status=404)