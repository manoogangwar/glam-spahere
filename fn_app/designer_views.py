from django.shortcuts import render, redirect
from .models import Designer,DesignerWork,TipsTricks,Message,User,Job
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone


def checkId(request):
    id=request.GET["des_id"]
    context={
        'status':Designer.objects.filter(d_ID__iexact=id).exists()
    }
    return JsonResponse(context)
#messages
def compose(request):
    key = request.session.get('session_key')
    uid = User(u_ID = key)
    msg = Message.objects.all()
    if request.method=="POST":
        did=request.POST['designer_id']
        dins = Designer.objects.get(d_ID=did)
        messages=request.POST["msg"]
        m_obj=Message(sender_id=uid,receiver_id=dins,message_text=messages)
        m_obj.save()
        return redirect('home')
    else:
        return redirect('home')


# post tips and tricks
def post_tips(request):
    key = request.session.get('session_key')
    user = None
    if key:
        try:
            user = User.objects.get(u_ID=key)
        except:
            try:
                user = Designer.objects.get(d_ID=key)
            except:
                user = None
    if request.method =="GET":
        return render(request,'fn_app/designer/add_tips.html',{'user':user})
    if request.method == 'POST':
        d_id=request.session["session_key"]
        c=request.POST["content"]
        d_obj=Designer.objects.get(d_ID=d_id)
        t=TipsTricks(designer=d_obj,content=c)
        t.save()
        messages.success(request, "Tips uploaded successfully")
        return render(request,'fn_app/designer/add_tips.html',{'user':user})
#upload works
def d_works_coll(request):
    key = request.session.get('session_key')
    user = None
    if key:
        try:
            user = User.objects.get(u_ID=key)
        except:
            try:
                user = Designer.objects.get(d_ID=key)
            except:
                user = None
    if request.method =="GET":
        return render(request,'fn_app/designer/d_workscoll.html', {'user':user})
    if request.method == 'POST':
        d_title=request.POST["title"]
        d_desc=request.POST["description"]
        d_year=request.POST["year"]
        d_client=request.POST["client"]
        d_pic=request.FILES["pic"]
        id=request.session["session_key"]
        designer_obj=Designer.objects.get(d_ID=id)
        work_obj=DesignerWork(designer= designer_obj, title=d_title, description=d_desc, year=d_year, client=d_client, photo=d_pic)
        work_obj.save()


    messages.success(request, "work uploaded successfully")
    return render(request,'fn_app/designer/d_workscoll.html', {'user':user})
    
        


def add_job(request):
    key = request.session.get('session_key')
    user = None
    if key:
        try:
            user = User.objects.get(u_ID=key)
        except:
            try:
                user = Designer.objects.get(d_ID=key)
            except:
                user = None 
        if request.method =="GET":
                return render(request,'fn_app/designer/add_job.html',{'user':user})
        if request.method == 'POST':
            designation=request.POST["designation"] 
            seats=request.POST["seats"]    
            mail=request.POST["mailing_link"]
            eligibility=request.POST["eligibility"]   
            profile=request.POST["profile"]  
            qualification=request.POST["qualification"]  
            location=request.POST["location"]  
            age=request.POST["age"]  
            salary=request.POST["salary"] 
            last_date=request.POST.get('date') 
            if not last_date:
                last_date = timezone.now
            # date field convert 
            id=request.session["session_key"]   
            designer_obj=Designer.objects.get(d_ID=id)
            job_obj=Job(designer= designer_obj, designation=designation, seats_available=seats, mailing_link=mail, eligibility=eligibility, work_profile=profile,min_qual=qualification,job_location=location,age_req=age, last_date=last_date ,salary_pkg=salary, )
            job_obj.save()
            if job_obj:
                messages.success(request, "Job Uploaded Successfully!")
        return render(request,'fn_app/designer/add_job.html',{'user':user})

# designer edit home 

def designer_edit_home(request):
    id=request.session.get('session_key')
    if id:
        try:
            user = Designer.objects.get(d_ID=id)
        except:
            return redirect('d_register')
        dg=Designer.objects.all()
        

    if request.method == 'POST':
        namechange=request.POST["name"]
        emailchange=request.POST["email"]
        phonechange=request.POST["phone"]
        citychange=request.POST["city"]
        aboutchange=request.POST["about"]
        id=request.session["session_key"]
        obj= Designer.objects.get(d_ID=id)
        obj.d_name=namechange
        obj.d_mail=emailchange
        obj.d_phone=phonechange
        obj.d_city=citychange
        obj.d_about=aboutchange
        obj.save()
        context={
        "obj_key":obj,
        'user':user,
        'desi':dg
        }
        return render(request,'fn_app/designer/designer_home.html',context)
    else:
        return render(request,'fn_app/designer/designer_edit_home.html',{'user':user, 'desi':dg})


# designer home 
def designer_home(request):
    id=request.session['session_key']
    designer_obj=Designer.objects.get(d_ID=id)
    user = None
    dg=Designer.objects.all()
    if id:
        try:
            user = User.objects.get(u_ID=id)
        except:
            try:
                user = Designer.objects.get(d_ID=id)
            except:
                return render(request,'fn_app/designer/designer_home.html')
            context={
        'obj_key': designer_obj,
        'user':user,
        'desi':dg
    }
    return render(request,'fn_app/designer/designer_home.html', context)
    
    
   


#  designer login function 

def designer_login(request):
    if request.method=='GET':   #httpProtocol method

        return render (request, 'fn_app/designer/d_register.html')
    
    if request.method=='POST':
        d_id=request.POST["d_id"]        #VARIABLE name can be changed
        d_pass=request.POST["d_password"]

        d_list =Designer.objects.filter( d_ID=d_id, d_password=d_pass)
        size=len(d_list)  
        print(size)
        if size>0:
        
            # print("designer exists")
            # binding id in session
            request.session['session_key']=d_id 
            designer_obj=Designer.objects.get(d_ID=d_id)
            context={'obj_key':designer_obj}

            return redirect('home')
        else:
            messages.error(request,"Invalid ID or Password!")  #for showing error message in the browser
            return render (request, 'fn_app/designer/d_register.html')

def d_register(request):
    dg=Designer.objects.all()
    if request.method=='GET':
        return render (request,'fn_app/designer/d_register.html',{'des':dg})
    if request.method=='POST':
        id=request.POST['d_id']
        password= request.POST['d_password']
        name = request.POST['d_name']
        email = request.POST['d_mail']
        phone = request.POST['d_phone']
        qualify=request.POST['d_qualification']
        state=request.POST['d_state']
        city=request.POST['d_city']
        gen=request.POST['d_gen']
        skill=request.POST['d_skills']
        about=request.POST['d_about']   
        pic= request.FILES.get('d_pic')                     
        registration_object=Designer(d_ID=id,d_password=password,d_name=name,d_mail=email,d_phone=phone,d_qualification=qualify,d_state=state,d_city=city,d_gender=gen,d_skills=skill,d_about=about, d_pic=pic)
        registration_object.save()
        if registration_object:
            messages.success(request, "Designer registration successful!")
        return render (request,'fn_app/designer/d_register.html', {'des':dg})
    

def all_collections(request):
    obj  = DesignerWork.objects.all()
    return render(request, 'fn_app/html/collections.html', {'obj':obj})