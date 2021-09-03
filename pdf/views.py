from django.shortcuts import render

from dashboard.models import Expenditure, Income

from dashboard.forms import IncomeSearchForm

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


# Search Income by Date Range and Generate PDF 
#def date_range_income_pdf(request):
   # listIncome = Income.objects.all()
    #searchForm = IncomeSearchForm(request.POST or None)

   # if request.method == 'POST':
      #  listIncome = Income.objects.filter(
        #description__icontains=searchForm['description'].value(),
       # date__range=[
                               # searchForm['start_date'].value(),
                                #searchForm['end_date'].value()
                           # ]
        #)
    #else:
       # searchForm = IncomeSearchForm()

    #context = {
      #  'listIncome':listIncome,
    #}
   # return render(request, 'cashier/search_income_range.html', context)

#def pdf_create_report_income_by_date(request):

    #list_income = Income.objects.order_by('-date')

    #template_path = 'pdf/pdfincomedate.html'

    #context = {'list_income': list_income}

   # response = HttpResponse(content_type='application/pdf')

    #response['Content-Disposition'] = 'filename="income_report_by_date.pdf"'

    # find the template and render it.
    #template = get_template(template_path)
   # html = template.render(context)

    # create a pdf
    #pisa_status = pisa.CreatePDF(
      # html, dest=response)
    # if error then show some funy view
    #if pisa_status.err:
      # return HttpResponse('We had some errors <pre>' + html + '</pre>')
    #return response


    

