from email.mime import application
from msilib.schema import Class
from statistics import mode
from django.db import models
from Hospital.models import Hospital

from unicodedata import name
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.db import connection
from django.template.loader import get_template
#from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class Vaccination_Info(models.Model):
    hospital_name = models.ForeignKey(Hospital,null=True,on_delete=models.SET_NULL)
    Frist_Dose = models.DateField(null=True)
    Second_Dose = models.DateField(null=True)
    Third_Dose = models.DateField(null=True)
    Vaccine_status = models.CharField(max_length=150,null=True)


    def ViewPDF(request,data):
        pdf = render_to_pdf('User/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def DownloadPDF(request,data):
        pdf = render_to_pdf('User/pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Covid Certificate_%s.pdf" %("12341231")
        content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response