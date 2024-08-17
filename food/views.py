from django.http import HttpResponse
from django.shortcuts import render,redirect
from food.models import Recipe


# Create your views here.


def index(request):
   if request.method == 'POST':
      r_name = request.POST.get('recipename')
      r_desc = request.POST.get('recipedescription')
      r_image = request.FILES.get('recipeimage')
      Recipe.objects.create(recipe_name=r_name, recipe_description=r_desc, recipe_image=r_image)
      return redirect('display_data')
   else:
      return render(request, 'index.html')

def display_data(request):
   all_data = Recipe.objects.all()
   return render(request,'display.html',{'data':all_data})


def delete_it(request,id):
   item = Recipe.objects.get(id=id)
   item.delete()
   return redirect('display_data')

def edit_it(request,id):
   item = Recipe.objects.get(id=id)
   if request.method == 'POST':
      item.recipe_name = request.POST.get('recipename')
      item.recipe_description = request.POST.get('recipedescription')
      if request.FILES.get('recipeimage'):
         item.recipe_image = request.FILES.get('recipeimage')
      
      item.save()
      return redirect('display_data')
   else:
      return render(request,'edit.html',{'e_item':item})
   

def seperate_view(request,id):
   data = Recipe.objects.get(id=id)
   return render(request,'seperate.html',{'data':data})