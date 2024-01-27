from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Membernew
from .forms import MemberForm



def allmember(request):
    member_list=Membernew.objects.all().values()
    context={
        'member_list':member_list
      }
    template=loader.get_template('allmember.html')
    return HttpResponse(template.render(context,request))

def detail(request,id):
    mymember=Membernew.objects.get(id=id)
    template=loader.get_template('detail.html')
    context={
            'mymember':mymember
        }
    return HttpResponse(template.render(context,request))


def add_newmember(request):
    template=loader.get_template('add_newmember.html')
    return HttpResponse(t1.render())

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())

@csrf_exempt
def add_newmember(request):
    if request.method == 'POST':
        firstname= request.POST.get('firstname',)
        lastname= request.POST.get('lastname',)   
        rollno= request.POST.get('rollno',)
        phoneno=request.POST.get('phoneno',)
        image=request.FILES['image']
        membernew=Membernew(firstname=firstname,lastname=lastname,rollno=rollno,phoneno=phoneno,image=image)
        membernew.save()
    template=loader.get_template('add_newmember.html')
    return HttpResponse(template.render())


def update(request,id):
    member=Membernew.objects.get(id=id)
    form=memberForm(request.POST,instance=member)
    if form.is_valid():
            form.save()
            t1=loader.get_template('add_newmember.html')
            return HttpResponse(t1.render())
    return render(request,'update.html',{'form':form,'member':member})    

@csrf_exempt
def delete(request,id):
    if request.method=='POST':
        member=Membernew.objects.get(id=id)
        member.delete()
        t1=loader.get_template('allmember.html')
        return HttpResponse(t1.render())
    return render(request,'delete.html')



    

