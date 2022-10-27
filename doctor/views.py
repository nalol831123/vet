from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import date
from .models import Register
from .forms import RegisterForm

# Create your views here.
def index(request):
    """ index page """
    return render(request, 'index.html')

def registered(request):
    """ registered page """
    RegisterCreate = Register.objects.all()  # 查詢所有資料
    Registerform = RegisterForm()

    if 'term' in request.GET:
        qs = Register.objects.filter(ID__icontains=request.GET.get('term'))
        print(request.GET)
        results = []
        for ds in qs:
            ds_json = {}
            ds_json['label'] = ds.ID
            ds_json['value'] = ds.ID
            ds_json['Animal'] = ds.Animal
            ds_json['Species'] = ds.Species
            ds_json['Sex'] = ds.Sex
            ds_json['Neuter'] = ds.Neuter
            ds_json['Age'] = ds.Age
            ds_json['Name'] = ds.Name
            ds_json['Phone'] = ds.Phone
            ds_json['Addr'] = ds.Addr
            ds_json['Doctor'] = ds.Doctor
            results.append(ds_json)
        return JsonResponse(results, safe=False)

    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/registered/")
    # show today's patient
    today = date.today()
    today = Register.objects.filter(UpdateTime__year=today.year, UpdateTime__month=today.month, UpdateTime__day=today.day)

    context = {
        'form': RegisterCreate,
        'Registerform': Registerform,
        'today': today
    }
    return render(request, 'registered.html', context)

def id_search(request):
    """ id_search """
    # get the input id
    if request.method == "GET":
        
        # search id in database
        instance = Register.objects.filter(ID=request.GET['ID']).first()
        form = RegisterForm(instance=instance)

        # show today's patient
        today = date.today()
        today = Register.objects.filter(UpdateTime__year=today.year, UpdateTime__month=today.month, UpdateTime__day=today.day)
        context = {
            'form': form,
            'today': today
        }

        return render(request, 'registered.html', context)

    return redirect('/registered')

def patient(request):
    """ index page """
    return render(request, 'patient.html')

def med(request):
    """ index page """
    return render(request, 'med.html')

def summary(request):
    """ index page """
    return render(request, 'summary.html')