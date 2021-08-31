from django.shortcuts import render

from dashboard.models import Expenditure, Income

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa


# Create your views here.
def show_income_pdf(request):
    list_income = Income.objects.all()
    context = {
        'list_income':list_income,
    }
    return render(request, 'pdf/showinfo.html', context)

def pdf_create_report_income(request):

    list_income = Income.objects.order_by('-date')

    template_path = 'pdf/pdfreport.html'

    context = {'list_income': list_income}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="income_report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    

