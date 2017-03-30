from django.shortcuts import render

from crm import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def dashboard(request):
    return render(request, 'crm/dashboard.html')


def customers(request):
    customer_list = models.Customer.objects.all()
    # 每页返回几条数据
    paginator = Paginator(customer_list, 1)
    page = request.GET.get('page')
    try:
        customer_objs = paginator.page(page)
    except PageNotAnInteger:
        customer_objs = paginator.page(1)
    except EmptyPage:
        customer_objs = paginator.page(paginator.num_pages)

    return render(request, 'crm/customers.html', {'customer_list': customer_objs})
