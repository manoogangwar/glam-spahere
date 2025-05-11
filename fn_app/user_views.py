from django.shortcuts import render,HttpResponse,redirect
from .models import User,Message,Designer,Job
from django.contrib import messages
from django.http import JsonResponse

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
    


def job_request(request):
    id=request.session['session_key']
    job=Job.objects.all()
    dg=Designer.objects.all()  
    if id:
        try:
            user = User.objects.get(u_ID=id)
        except:
            try:
                user = Designer.objects.get(d_ID=id)
            except:
                user = None
        context={'user':user,
                "des":dg, 
                'obj':job
                }
        return render(request,"fn_app/user/job_request.html",context,)

    
#logout
def logout(request):
    request.session.flush() #clering all the values bind in that session
    return redirect("home")


def user_edit_home(request):
    id = request.session.get('session_key')
    dg = Designer.objects.all()
    if id:
        try:
            user = User.objects.get(u_ID=id)
        except:
            return redirect('user_registration')
            
    else:
        return redirect('user_registration')
    
    if request.method == 'POST':
        namechange=request.POST["name"]
        emailchange=request.POST["email"]
        phonechange=request.POST["phone"]
        citychange=request.POST["city"]
        id=request.session["session_key"]
        obj= User.objects.get(u_ID=id)
        obj.u_name=namechange
        obj.u_mail=emailchange
        obj.u_phone=phonechange
        obj.u_city=citychange
        obj.save()
        return redirect('user_home')
    else:
        return render(request,'fn_app/user/user_edit_home.html',{
        "user":user,
        'obj_key':user, 
        'desi':dg})






def user_home(request):
 
    id=request.session['session_key']
    msg = Message.objects.all()
    d_obj=Designer.objects.all()
    user_obj=User.objects.get(u_ID=id)
        
    if id:
        try:
            user = User.objects.get(u_ID=id)
        except:
            try:
                user = Designer.objects.get(d_ID=id)
            except:
                user = None
        context={'obj_key':user_obj, 'msg':msg ,"d_key":d_obj, 
                 'user':user}
        return render(request,"fn_app/user/user_home.html",context)


def user_login(request):
    if request.method=='GET':   #httpProtocol method

        return render (request, 'fn_app/user/user_reg.html')
    
    if request.method=='POST':
        user_id=request.POST["id"]        #VARIABLE name can be changed
        user_pass=request.POST["password"]

        user_list =User.objects.filter( u_ID=user_id, u_password=user_pass)
        size=len(user_list)  
        if size>0:
            # binding id in session
            request.session['session_key']=user_id 
            
            return redirect('home')
        else:
            messages.error(request,"Invalid ID or Password!")  #for showing error message in the browser
            return render (request, 'fn_app/user/user_reg.html')
        

def user_reg(request):
    dg=Designer.objects.all()
    if request.method=='GET':
        return render (request,'fn_app/user/user_reg.html',{'des':dg})
    if request.method=='POST':
        id=request.POST['id']
        password= request.POST['password']
        name = request.POST['name']
        email = request.POST['mail']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        pic=request.FILES.get('pic')
        registration_user=User(u_ID=id,u_password=password,u_name=name,u_mail=email,u_gender=gender,u_phone=phone, u_address=address,u_state=state,u_city=city,u_pic=pic)
        registration_user.save()

        if registration_user:
            messages.success(request, "User registration successful!")
        return render (request,'fn_app/user/user_reg.html', {'des':dg})