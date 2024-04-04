from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template=loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))  

def custom404(request, exception):
  template = loader.get_template('404.html')
  return HttpResponse(template.render({}, request), status=404)

def testing(request):
  template = loader.get_template ('template.html')
  context = {
    'firstname': 'Ann',
  }
  return HttpResponse(template.render(context,request))


def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers':mymembers,
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
      }]   
  }
  return HttpResponse(template.render(context, request))

def members(request):
  mymembers = Member.objects.all()
  template = loader.get_template('template.html')
  return render(request, 'template.html', {'mymembers': mymembers})

def testing(request):
  mydata = Member.objects.all().order_by('-lastname', 'id').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata
  }
  return HttpResponse(template.render(context, request))