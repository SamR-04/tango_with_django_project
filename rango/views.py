from rango.models import Category
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    # queries the category model to retreive the top 5 catagories , sortes in descending order  and nonly the friirst 5 

    context_dict= {}
    context_dict['noldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories']= category_list

    return render(request, 'rango/index.html', context = context_dict)
    #return HttpResponse ('Rango says hey there partner! <a href="/rango/about/">About</a>')
                         
def about(request):
    return render(request, 'rango/about.html')
    #return HttpResponse('Rango says here is the about page. <a href="/rango/">Index</a>')
    

