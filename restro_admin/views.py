from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic.base import View
from restro_admin.models import *
from restro_admin.forms import *


def admin_login(request):
    return render(request,'restro_admin/login.html')


def admin_home(request):
    return render(request,'restro_admin/admin-home.html')


def admin_login_check(request):
    ausername = request.POST.get("admin_username")
    apassword = request.POST.get("admin_password")
    try:
        AdminLoginModel.objects.get(username=ausername,password=apassword)
        request.session ['santosh'] = True
        return redirect('admin-home')

    except AdminLoginModel.DoesNotExist:
        messages.error(request,"Sorry Invalid Details")
        return redirect('admin-login')


def admin_logout(request):
    request.session ['santosh'] = False
    return redirect('admin-login')


#state
def open_state(request):
    return render(request,'restro_admin/open_state.html',{"sf":StateForm(),"sdata":StateModel.objects.all()})


def save_state(request):
    sf = StateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_state')
    else:
        return render(request,"restro_admin/open_state.html",{"sf":sf})


def update_state(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno":sno,"sname":sname}
    return render(request,"restro_admin/open_state.html",{"update_data":d1,"sdata":StateModel.objects.all()})


def update_state_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    StateModel.objects.filter(state_no = sno).update(state_name=sname)
    return redirect('open_state')


def delete_state(request):
    sno = request.GET.get("sno")
    StateModel.objects.filter(state_no=sno).delete()
    return redirect('open_state')


#city
def open_city(request):
    return render(request,'restro_admin/open_city.html',{"sf":CityForm(),"sdata":CityModel.objects.all()})


def save_city(request):
    sf = CityForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_city')
    else:
        return render(request, "restro_admin/open_city.html", {"sf": sf})


def update_city(request):
    return None


def update_city_data(request):
    return None


def delete_city(request):
    return None


class AreaView(View):

    def get(self,request):
        form = AreaForm()
        data = AreaModel.objects.all()
        return render(request,'restro_admin/open_area.html',{'form':form,'data':data})

    def post(self,request):
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area')


#type
def open_type(request):
    return render(request, 'restro_admin/open_type.html', {"sf": RestaurantTypeForm(), "sdata": RestaurantTypeModel.objects.all()})


def save_type(request):
    sf = RestaurantTypeForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_type')
    else:
        return render(request, "restro_admin/open_type.html", {"sf": sf})



