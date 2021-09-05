from django.shortcuts import render

from .models import Pie


def index(request):
    """馅饼店的主页"""
    return render(request, 'pies/index.html')


def pies(request):
    """显示所有的馅饼"""
    pies = Pie.objects.order_by('date_added')
    context = {'pies': pies}
    return render(request, 'pies/pies.html', context)


def pie(request, pie_id):
    """显示单一馅饼的全部信息"""
    pie = Pie.objects.get(id=pie_id)
    toppings = pie.topping_set.order_by('-date_added')
    context = {'pie': pie, 'toppings': toppings}
    return render(request, 'pies/pie.html', context)
