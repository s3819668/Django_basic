from django.http import HttpResponse
from TestModel.models import Test

def add(request):
    name=request.GET.get('name')
    age=request.GET.get('age')
    test=Test(name=name,age=age)
    test.save()
    return HttpResponse("success")

def get_all(request):
    arr=Test.objects.all()
    response=""
    for people in arr:
        response+=people.name +" "
    return HttpResponse("<p>"+response+"</p>")
def update(request):
    id = request.GET.get('id')
    test=Test.objects.get(id=id)
    test.name="NoName"
    test.save()
    return HttpResponse("update")
def delete(request):
    id=request.GET.get('id')
    test=Test.objects.get(id=id)
    test.delete()
    return HttpResponse("delete")