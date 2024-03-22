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

# def custom_404(request, exception):
#     return render(request, '404.html', status=404)
# def 404(request):
#   mymembers = 404.objects.all().values()
#   template = loader.get_template('404.html')
#   context = {
#     'mymembers': mymembers,
#   }
# return render(request, '404.html', status=404)
