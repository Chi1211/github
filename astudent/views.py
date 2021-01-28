from django.shortcuts import render
from .models import StudentModel
from django.views import View
from django.http import HttpResponse
# from django.contrib.redirects.models import Redirect

# Create your views here.
def getstu():
	students=StudentModel.objects.all()
	context={'students': students}
	return context

class GetStudent(View):
	def get(self, request):
		context=getstu()
		return render(request, 'astudent/menu.html', context)

class AddStudent(View): 
	def get(self, request):
		context=getstu()
		return render(request, 'astudent/add.html')
	def post(self, request):
		# if first_name and last_name and birthday and address:
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		birthday=request.POST['birthday']
		address=request.POST['address']
		StudentModel.objects.create(first_name=first_name, last_name=last_name, birthday=birthday, address=address)
		context=getstu()
		return render(request, 'astudent/menu.html', context)

class UpdateStudent(View): 
	def get(self, request, id):
		students=StudentModel.objects.get(id=id)
		context={'students': students}
		return render(request, 'astudent/update.html', context)
	def post(self, request, id):
		# if first_name and last_name and birthday and address:
		students=StudentModel.objects.get(id=id)
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		birthday=request.POST['birthday']
		address=request.POST['address']
		students.first_name=first_name
		students.last_name=last_name
		students.birthday=birthday
		students.address=address
		students.save()
		context=getstu()
		return render(request, 'astudent/menu.html', context)

def DeleteStudent(request, id):
	destudent=StudentModel.objects.filter(id=id)
	destudent.delete()
	context=getstu()
	return render(request, 'astudent/menu.html', context)

def Search(request):
	students=StudentModel.objects.filter(first_name__contains=request.POST['search'])
	context={'students': students}
	return render(request, 'astudent/menu.html', context)