from django.shortcuts import render , redirect, HttpResponse
from .models import Users , Finalresults,Aptitude,Technical,Listquestions,quizattempt,quizattempt1,Category,Check_Select,Aptitude1,Technical1,Aptitude2,Technical2
from django.conf import settings
from django.contrib import messages
from random import sample
import datetime
import csv
import xlwt
import random
from django.http import request
from PIL import Image, ImageDraw, ImageFont 
import pandas as pd 

# Create your views here.
def testlogin(request):
    return render(request,"testlogin.html")

def index(request):
    return render(request,"index.html")
    

def signup(request):
    #return render(request,"signup.html")
    return render(request,"testlogin.html")

def login(request):
    #return render(request,'login.html')
    return render(request,"testlogin.html")

def userloginview(request):
    #return render(request,'login.html')
    return render(request,"testlogin.html")

def aboutus(request):
    return render(request,'aboutus.html')

def forgot(request):
    return render(request,'forgot.html')

def userregister(request):
    name=request.POST["name"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    college = request.POST["college"]
    password=request.POST["password"]
    re_password=request.POST["re_password"]
    
    if Users.objects.filter(email=email).exists():
        messages.add_message(request,messages.ERROR,"Username Already Exist Login")
        return redirect(index)
    else:    
        Users(name=name,email=email,phone=phone,password=password,re_password=re_password,college=college,role='user').save()
        messages.add_message(request,messages.ERROR,"You Register Succesfully Login Now!")
        return redirect('userloginview')
 
def userauthentication(request):
    email=request.POST['email'] #session
    password=request.POST['password'] 
    if Users.objects.filter(email=email).exists():
        a= Users.objects.get(email=email)
        if password==a.password:
            request.session['email']=a.email
            request.session['name']=a.name
            request.session['role']=a.role
            request.session['college']=a.college
            request.session['phone']=a.phone
            request.session['logged_in']=True
            request.session['quizstart']=False
            
            if request.session['email']=="admin":
                return redirect('index')
                
            else:
                return redirect('userhome')
        else:
            messages.add_message(request,messages.ERROR,"Invalid Username or Password")
            return redirect('userloginview')
    else:
        messages.add_message(request,messages.ERROR,"Username Does Not Exist Need To Register First")
        return redirect(index)


def userhome(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    else:
        if request.session['quizstart']==True:
            return redirect('quizquestions')
        else:
            user=Users.objects.get(email=request.session["email"])
            a=datetime.datetime.now() 
            request.session['strtime']=str(a)
            request.session['result'] = False
            sub = Category.objects.all()
            return render(request,'userhome.html',{"user":user,"subjects":sub})



def instructions1(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    else:
        if request.session['quizstart']==True:
            return redirect('quizquestions')
        else:
            user=Users.objects.get(email=request.session["email"])
            a=datetime.datetime.now() 
            request.session['strtime']=str(a)
            request.session['result'] = False
            return render(request,"instructions1.html",{"user":user})

def instructions2(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    else:
        if request.session['quizstart']==True:
            return redirect('quizquestions')
        else:
            user=Users.objects.get(email=request.session["email"])
            a=datetime.datetime.now() 
            request.session['strtime']=str(a)
            request.session['result'] = False
            return render(request,"instructions2.html",{"user":user})

def quizquestions(request):
    if quizattempt.objects.filter(Name=request.session['name']).exists():
        messages.add_message(request,messages.ERROR,"Already Submitted Ur Test")
        return redirect(index)
    
    else:
        apti=Aptitude.objects.all()
        countapti=Aptitude.objects.all().count() 
        tech=Technical.objects.all()
        counttech=Technical.objects.all().count()
        print('hi')
        if request.session['quizstart']!=True: #email 
            print("hello")
            aptilist = sample(list(apti),k=15)
            #aptilist=sample(list(apti),countapti) 
            techlist = sample(list(tech),k=15)
            #techlist=sample(list(tech),counttech) 
    
            request.session['quizstart']=True
            for i in aptilist:
                q=Listquestions()
                q.username = request.session['email']
                q.qid=i.qid
                q.Question=i.Question
                q.optionA=i.optionA
                q.optionB=i.optionB
                q.optionC=i.optionC
                q.optionD=i.optionD
                q.correct=i.correct
                q.qtype='apti'
                q.save()
            for i in techlist:
                q=Listquestions()
                q.username = request.session['email']
                q.qid=i.qid
                q.Question=i.Question
                q.optionA=i.optionA
                q.optionB=i.optionB
                q.optionC=i.optionC
                q.optionD=i.optionD
                q.correct=i.correct
                q.qtype='tech'
                q.save()  

            

            aptilist1=Listquestions.objects.filter(qtype="apti")
            techlist1=Listquestions.objects.filter(qtype="tech")

            return render(request,'quizquestions.html',{"aptilist1": aptilist,"techlist1": techlist})   
        else:
            aptilist1=Listquestions.objects.filter(qtype="apti")
            techlist1=Listquestions.objects.filter(qtype="tech")

            return render(request,'quizquestions.html',{"aptilist1": aptilist,"techlist1": techlist})


def quizquestions1(request):
    if quizattempt.objects.filter(Name=request.session['name']).exists():
        messages.add_message(request,messages.ERROR,"Already Submitted Ur Test")
        return redirect(quizquestions2)
    else:
        messages.add_message(request,messages.ERROR,"pls attempt first quiz first")
        return redirect(index)

def quizquestions2(request):
    if quizattempt1.objects.filter(Name=request.session['name']).exists():
        messages.add_message(request,messages.ERROR,"Already Submitted Ur Test")
        return redirect(index)
    else:
        apti=Aptitude1.objects.all() 
        tech=Technical1.objects.all()
        countapti=Aptitude1.objects.all().count() 
        counttech=Technical1.objects.all().count()
        print('hi')
        if request.session['quizstart']!=True: #email 
            print("hello")
            aptilist = sample(list(apti),k=15)
            techlist = sample(list(tech),k=15)
            #aptilist=sample(list(apti),countapti) 
            #techlist=sample(list(tech),counttech) 
        
            request.session['quizstart']=True
            for i in aptilist:
                q=Listquestions()
                q.username = request.session['email']
                q.qid=i.qid
                q.Question=i.Question
                q.optionA=i.optionA
                q.optionB=i.optionB
                q.optionC=i.optionC
                q.optionD=i.optionD
                q.correct=i.correct
                q.qtype='apti'
                q.save()
            for i in techlist:
                q=Listquestions()
                q.username = request.session['email']
                q.qid=i.qid
                q.Question=i.Question
                q.optionA=i.optionA
                q.optionB=i.optionB
                q.optionC=i.optionC
                q.optionD=i.optionD
                q.correct=i.correct
                q.qtype='tech'
                q.save()  



            aptilist1=Listquestions.objects.filter(qtype="apti")
            techlist1=Listquestions.objects.filter(qtype="tech")

            return render(request,'quizquestions.html',{"aptilist1":aptilist,"techlist1":techlist})   
        else:
            aptilist1=Listquestions.objects.filter(qtype="apti")
            techlist1=Listquestions.objects.filter(qtype="tech")

            return render(request,'quizquestions.html',{"aptilist1":aptilist,"techlist1":techlist})
    

def logoutuser(request):
    del request.session['name']
    del request.session['role']
    del request.session['phone']
    del request.session['email']
    request.session['logged_in']=False 
    messages.add_message(request,messages.ERROR,"Logout Successfully")
    return redirect(testlogin)
    

        
def forgotpass(request):
    email=request.POST['email']
    phone=request.POST['phone']  
    if Users.objects.filter(email=email).exists():
        a= Users.objects.get(email=email)
        if phone==a.phone:
            request.session['usernameid']=a.email
            return redirect("changepassview")
        else:
            messages.add_message(request,messages.ERROR,"Phone Number Didn't Match")
            return redirect("forgot")
    else:
        messages.add_message(request,messages.ERROR,"Username Does Not Exist Need To Register First")
        return redirect(index)
        

    
def changepassview(request):
    return render(request,"changepass.html")   

def changepass(request):
    s=Users.objects.get(email=request.session["usernameid"])
    s.password=request.POST['password']
    s.save()
    messages.add_message(request,messages.ERROR,"Password Change Succesfully! Login Now")
    return redirect(index) 
   


 

def profile(request):
    if request.method == "GET":
        return render(request,"profile_new.html")
    else:
        a = Users.objects.get(email=request.session['email'])
        a.email=request.POST["email"]
        a.phone = request.POST["phone"]
        a.college = request.POST["college"]
        a.SSC = request.POST["SSC"]
        a.marks2 = request.POST["marks2"]
        a.HSC = request.POST["HSC"]
        a.marks1 = request.POST["marks1"]
        a.graduation = request.POST["graduation"]
        a.marks3 = request.POST["marks3"]
        a.post_graduation = request.POST["post_graduation"]       
        a.marks4 = request.POST["marks4"]
        a.certification = request.POST["certification"]
        a.company1 = request.POST["company1"]
        a.company2 = request.POST["company2"]
        a.designation = request.POST["designation"]
        a.box1 = request.POST["box1"]
        a.box2 = request.POST["box2"]
        a.Salary1 = request.POST["Salary1"]
        a.Salary2 = request.POST["Salary2"]
        a.skills = request.POST["skills"]
        a.Accomplishment = request.POST["Accomplishment"]
        a.Hobby = request.POST["Hobby"]
        a.References = request.POST["References"]
        a.DOB = request.POST['DOB']
        a.gender = request.POST["gender"]
        a.address = request.POST["address"]
        a.Languages = request.POST["Languages"]
        a.img = request.POST["img"]
        a.save()
        return redirect(profile_details)

def profile_details(request):
    obj = Users.objects.get(email=request.session['email'])
    context = {
        'email' : obj.email,
        'phone': obj.phone,
        'college' : obj.college,
        'HSC' : obj.HSC,
        'marks1' : obj.marks1,
        'SSC' : obj.SSC,
        'marks2' : obj.marks2,
        'graduation' : obj.graduation,
        'marks3' : obj.marks3,
        'post_graduation' : obj.post_graduation,
        'marks4' : obj.marks4,
        'certification' : obj.certification,
        'company1' : obj.company1,
        'designation' : obj.designation,
        'company2' : obj.company2,
        'box1' : obj.box1,
        'box2' :obj.box2,
        'Salary1' : obj.Salary1,
        'Salary2' : obj.Salary2,
        'skills' : obj.skills,
        'Accomplishment' : obj.Accomplishment,
        'Hobby' : obj.Hobby,
        'References' : obj.References,
        'DOB': obj.DOB,
        'gender' : obj.gender,
        'address' : obj.address,
        'Languages': obj.Languages,
        'img'  : obj.img ,
    }
    return render(request,"profile_details.html",context)

def passstudentsview(request): 
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    elif("admin" not in request.session['role']):
        messages.add_message(request,messages.ERROR,"You Dont have Permission Access This Page")
        return redirect(index) 

    else:
        return render(request,'passstudents.html')

def passstudentslist(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    elif("admin" not in request.session['role']):
        messages.add_message(request,messages.ERROR,"You Dont have Permission Access This Page")
        return redirect(index)

    else:
        return render(request,'passstudentslist.html')

def passstudents(request):  
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    elif("admin" not in request.session['role']):
        messages.add_message(request,messages.ERROR,"You Dont have Permission Access This Page")
        return redirect(index)
      
    else: 
        a=request.GET["college"]
        request.session['coll']=a
        coll=Finalresults.objects.filter(college=str(a))
        return render(request,'passstudentslist.html',{"coll":coll})

def result(request):
    if(not request.session['logged_in']):
        return redirect(userloginview)
    else:
        c=datetime.datetime.now() 
        request.session['endtime']=str(c)
        a=int(request.session['aptimarks'])
        total=(a)*2
        request.session['total']=total    
        Listquestions.objects.all().delete()
        request.session['quizstart']=False
        request.session['result'] = True

    if quizattempt.objects.filter(Name=request.session['name']).exists():
        q=quizattempt1()
        q.Name=request.session['name']
        q.Email=request.session['email']
        q.save()
    else:
        q=quizattempt()
        q.Name=request.session['name']
        q.Email=request.session['email']
        q.save()

    if total > 20:
        d=Users.objects.get(email=request.session["email"])
        a=Finalresults()
         #a.sid=d.id
        a.name=d.name
        a.email=d.email
        a.college =d.college
        a.phone=d.phone
        a.strtime=request.session['strtime']
        a.endtime=request.session['endtime']
        a.marks=request.session['total'] 
        a.save()
        return render(request,'result.html')
    else:
        d=Users.objects.get(email=request.session["email"])
        a=Finalresults()
        #a.sid=d.id
        a.name=d.name
        a.email=d.email
        a.college =d.college
        a.phone=d.phone
        a.strtime=request.session['strtime']
        a.endtime=request.session['endtime']
        a.marks=request.session['total'] 
        a.save()
        return render(request,'result.html')

def quizresult(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    else:
        if request.session.get('result'):
            del request.session['result']
            messages.add_message(request,messages.ERROR,"You Already Submited your Test")
            return redirect(index)
        
        else:
            print("hi")
            marks=0
            data = request.POST.items()
            #list
            for key,value in data:   
                print(key,value)
                
                try:
                    question = Check_Select.objects.get(qid=int(key))
                except:
                    pass
                else:
                    if(question.correct == value ):
                        marks +=1
                
            request.session['aptimarks']=marks
            return redirect('result')

def demo(request):
    return render(request,"technical.html")
    
def download(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    elif("admin" not in request.session['role']):
        messages.add_message(request,messages.ERROR,"You Dont have Permission Access This Page")
        return redirect(index)
        
    else:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="QuizPassstudents.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Name','Email Address','','','','Total Marks', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Finalresults.objects.filter(college=request.session['coll']).values_list('name', 'email', 'branch', 'year','div','marks')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)

        return response

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Name','Email','Department', 'Marks'])

    for student in Finalresults.objects.all().values_list('name','email','college','marks'):
        writer.writerow(student)

    response['Content-Disposition'] = 'attachment; filename="passstudents.csv"'

    return response 