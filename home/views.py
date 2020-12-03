
from django.urls import path
from home.models import Personal,Address,Salary,Otherincomee

from django.shortcuts import render, redirect
 
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse  
from home.functions import handle_uploaded_file  
from home.forms import StudentForm  
from .models import *

# Create your views here.

def index(request):
    return render(request,'personal.html')
def addresss(request):
    return render(request,'Address.html')
def salaryy(request):
    return render(request,'Salary.html')
def otherincome(request):
    return render(request,'Otherincome.html')
def house(request):
    return render(request,'HouseProperty.html')
def capital(request):
    return render(request,'CapitalGain.html')
def deduction(request):
    return render(request,'Deductions.html')
def morededuction(request):
    return render(request,'MoreDeductions.html')
def otherdeduction(request):
    return render(request,'EvenMoreDeductions.html')
def investmentdetails(request):
    return render(request,'TdsSummary.html')
def tds(request):
    return render(request,'AddTds.html')
def upload(request):
    return render(request,'Upload.html')

def selftax(request):
    return render(request,'TaxesPaidSummary.html')    

def personal(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        mid=request.POST.get('mid')
        last_name=request.POST.get('last_name')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        pan_number=request.POST.get('pan_number')
        father_name=request.POST.get('father_name')
        
        marital_status=request.POST.get('marital_status')
        personal=Personal(first_name=first_name,mid=mid,last_name=last_name,gender=gender,dob=dob,pan_number=pan_number,father_name=father_name,marital_status=marital_status)
        personal.save()
    return render(request,'Address.html')

def address(request):
    if request.method=='POST':
        flat_num=request.POST.get('flat_num')
        premise_name=request.POST.get('premise_name')
        road_name=request.POST.get('road_name')
        pincode=request.POST.get('pincode')
        area =request.POST.get('area')
        town_name=request.POST.get('town_name')
        state_name=request.POST.get('state_name')
        country_name=request.POST.get('country_name')
        contact_number=request.POST.get('contact_number')
        email=request.POST.get('email')
        email2=request.POST.get('email2')
        address=Address(flat_num=flat_num,premise_name=premise_name,road_name=road_name,pincode=pincode,area=area,town_name=town_name,state_name=state_name,country_name=country_name,contact_number=contact_number,email=email,email2=email2)
        address.save()
    return render(request,'Salary.html')

def salary(request):
    if request.method=='POST':
        employer_name=request.POST.get('employer_name')
        employer_type=request.POST.get('employer_type')
        salary=request.POST.get('salary')
        perquisites=request.POST.get('perquisites')
        profit=request.POST.get('profit')
        allowances=request.POST.get('allowances')
        balance=request.POST.get('balance')
        #deduction=request.POST.get('deduction')
        std_deduciton=request.POST.get('std_deduciton')
        professional_tax=request.POST.get('professional_tax')
        income_chargeable=request.POST.get('income_chargeable')
        tds=request.POST.get('tds')
        tan=request.POST.get('tan')
        sal=Salary(employer_name=employer_name,employer_type=employer_type,salary=salary,perquisites=perquisites,
        profit=profit,allowances=allowances,balance=balance,std_deduciton=std_deduciton,
        professional_tax=professional_tax,income_chargeable=income_chargeable,tds=tds,tan=tan)
        sal.save()
    return render(request,'OtherIncome.html')

def uploadd(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"testing.html",{'form':student}) 

def otherincomeee(request):
    if request.method=="POST":
        saving_bank=request.POST.get('savings')
        deposit=request.POST.get('deposit')
        other=request.POST.get('other')
        oi=Otherincomee(saving_bank=saving_bank,deposit=deposit,other=other)
        oi.save()
        return render(request,'Address.html')
        
    return render(request,'Address.html')


def uploader(request):
    if request.method=="POST" and  request.FILES['file']:
        name = request.POST.get('name', '')
        file = request.FILES['file']

        doc=DocumentUpload(name=name,upload_file=file)
        doc.save()
        return redirect('salary')
    else:
        return render(request, 'fileupload.html')



