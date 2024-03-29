from django.http import HttpResponse
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
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
   'members': [
  {
    'id': 1,
    'firstname': 'Emil',
    'lastname': 'Refsnes',
    'phone': 5551234,
    'joined_date': mymembers.joined_date(2022, 1, 5)
  },
  {
    'id': 2,
    'firstname': 'Tobias',
    'lastname': 'Refsnes',
    'phone': 5557777,
    'joined_date': mymembers.joined_date(2021, 4, 1)
  },
  {
    'id': 3,
    'firstname': 'Linus',
    'lastname': 'Refsnes',
    'phone': 5554321,
    'joined_date': mymembers.joined_date(2021, 12, 24)
  },
  {
    'id': 4,
    'firstname': 'Lene',
    'lastname': 'Refsnes',
    'phone': 5551234,
    'joined_date': mymembers.joined_date(2021, 5, 1)
  },
  {
    'id': 5,
    'firstname': 'Stalikken',
    'lastname': 'Refsnes',
    'phone': 5559876,
    'joined_date': mymembers.joined_date(2022, 9, 29)
  }
],
  }
  return HttpResponse(template.render(context, request))