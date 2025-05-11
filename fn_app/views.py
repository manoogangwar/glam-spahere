from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from.models import *
from django.contrib import messages
# Create your views here.
#news update
def news_update(request):
    news_list=News.objects.all() #eqivalent to select*from event#
    # how to send data from views to template
    dg=Designer.objects.all()
    key = request.session.get('session_key')
    user = None
    if key:
        try:
            user = User.objects.get(u_ID = key)
        except:
            try:
                user = Designer.objects.get(d_ID=key)
            except:
                return render(request, 'fn_app/html/news.html',{context})
    context={
        "news_key":news_list,
        'des':dg,
        'user':user
    }

    return render(request, 'fn_app/html/news.html',context)


def work_detail(request,id):
    if request.method=="GET":
        dg=Designer.objects.get(d_ID=id)

        work_list =DesignerWork.objects.filter(designer=dg)
        context={"works":work_list,
                 "desi":dg
                 
                 } 
        return render(request,"fn_app/designer/designer_works.html",context)
# morefeedback
def more_feedback(request):
    feedback_list=FeedBack.objects.all()
    context={'feedback_key':feedback_list}
    return render(request, 'fn_app/html/all_feedbacks.html/' ,context) 

def home(request):
   #feedback show query here 
    user = None
    key = request.session.get('session_key')
    msg = Message.objects.all()
    d_obj=Designer.objects.all()
    feedback=FeedBack.objects.all()
    feedback_list=FeedBack.objects.order_by()[2:]
    event = Event.objects.all()
    dg=Designer.objects.all()
    tips=TipsTricks.objects.all()
    
    if key:
        try:
            user = User.objects.get(u_ID=key)
            return render(request,'fn_app/html/index.html',{"feedback_key":feedback_list,"feedback":feedback,'event_key':event, "des":dg, "tip":tips, 'user':user, 'msg':msg ,"d_key":d_obj,})
        except:
            try:
                user = Designer.objects.get(d_ID= key)
                return render(request,'fn_app/html/index.html',{"feedback_key":feedback_list,"feedback":feedback, "des":dg, "tip":tips,'event_key':event, 'user':user, 'msg':msg ,"d_key":d_obj,  })
            except:
                return render(request,'fn_app/html/index.html',{"feedback_key":feedback_list,"feedback":feedback, "des":dg, "tip":tips,'event_key':event, 'user':user, 'msg':msg ,"d_key":d_obj,  })
    return render(request,'fn_app/html/index.html',{"feedback_key":feedback_list, "des":dg,"feedback":feedback, "tip":tips, 'user':user,'event_key':event, 'msg':msg ,"d_key":d_obj,  })

def contactus(request):
    dg = Designer.objects.all()
    if request.method=='GET':
        return render(request,'fn_app/html/contact_us.html',{'des':dg} )
    if request.method=='POST':
# fetching data from html controls 
        user_name=request.POST["name"]
        user_email= request.POST["email"]
        user_phone= request.POST["phone"]
        user_query= request.POST["question"]
        #creating object
        contactus_object=Contact(name=user_name, email=user_email,phone=user_phone,question=user_query)
        #save the object
        contactus_object.save()
        messages.success(request, 'Thank u for contacting us')
        return render(request, 'fn_app/html/contact_us.html',{'des':dg} )
        
def feedback(request):
    dg = Designer.objects.all()

    try:
        obj = User.objects.get(u_ID=request.session.get('session_key'))
    except User.DoesNotExist:
        return redirect('user_registration')



    if request.method=='GET':
        return render(request,'fn_app/html/feedback.html', {'des':dg, 'user':obj})
    if request.method=='POST':
# fetching data from html controls 
        user_name=request.POST["name"]
        user_email= request.POST["email"]
        user_remark= request.POST["remark"]
        user_rating=request.POST['rating']
        #creating object
        feedback_object=FeedBack(name=user_name, email=user_email,remarks=user_remark, rating=user_rating)
        #save the object
        feedback_object.save()
        messages.success(request, 'Thank you for your feedback!')
        return render(request, 'fn_app/html/feedback.html',{'des':dg})

def about(request):
    obj = Designer.objects.all()
    dg=Designer.objects.all()
    return render(request, 'fn_app/html/about.html', {'obj':obj, 'des':dg})

def event_update(request):
    event_list=Event.objects.all() #eqivalent to select*from event#
    # how to send data from views to template
    dg=Designer.objects.all()
    key = request.session.get('session_key')
    user = None
    if key:
        try:
            user = User.objects.get(u_ID = key)
        except:
            try:
                user = Designer.objects.get(d_ID=key)
            except:
                return render(request, 'fn_app/html/events_updates.html',{'des':dg, 'event_key':event_list})

    context={
        'des':dg,
        "event_key":event_list,
        'user':user
    }
    return render(request, 'fn_app/html/events_updates.html',context)



def chat(request, id):
    key = request.session.get('session_key')
    if key:
        try:
            user = User.objects.get(u_ID=key)
        except User.DoesNotExist:
            return redirect('user_reg')

        receiver = get_object_or_404(Designer, d_ID=id)

        if request.method == 'POST':

            message = request.POST.get('message', '')
            if message:
                chat_message = Message()
                chat_message.user = user
                chat_message.designer = receiver
                if isinstance(user, User):
                    chat_message.user_message = message
                elif isinstance(user, Designer):
                    chat_message.designer_message = message
                chat_message.save()
                return redirect('chat', id=id)
        else:

            chat_messages = Message.objects.filter(user=user, designer=receiver)
            return render(request, 'fn_app/html/chat.html', {'user': user, 'receiver': receiver, 'chat_messages': chat_messages})
    return redirect('user_registration')



def designer_messages(request):
    q = request.GET.get('q', request.session.get('selected_user_id', 'abc07')).strip()
    key = request.session.get('session_key')
    user  = User.objects.get(u_ID=q)
    designer = Designer.objects.get(d_ID=key)
    if key:
        all_messages = Message.objects.filter(designer=designer).order_by('user')
        chat_messages = Message.objects.filter(user=user, designer=designer)
        distinct_users = []
        messages = []
        for message in all_messages:
            if message.user not in distinct_users:
                distinct_users.append(message.user)
                messages.append(message)
        if request.method == 'POST':

            message = request.POST.get('message', '')
            print(message)
            if message:
                chat_message = Message() 
                chat_message.user = user
                chat_message.designer = designer
                chat_message.designer_message = message
                chat_message.save()
                request.session['selected_user_id'] = q
                return redirect('designer_messages')
        return render(request, 'fn_app/designer/chat.html', {'msg': messages, 'user':designer,'receiver': user, 'chat_messages': chat_messages })
    else:
        return redirect('user_registration')
    

def send_message(request, id):
    key = request.session.get('session_key')
    user = get_object_or_404(User, u_ID=id)
    designer = Designer.objects.get(d_ID=key)
    msg = Message.objects.filter(user=user, designer=designer)
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            user = get_object_or_404(User, u_ID=id)
            Message.objects.create(user=user, designer=designer, designer_message=message)
            return render(request, 'fn_app/designer/send_message.html', {'msg': msg,'u':user, 'user':designer})
    else:
        return render(request, 'fn_app/designer/send_message.html', {'msg': msg,'u':user,'user':designer})
                                                            

def userchat(request):
    q = request.GET.get('q', request.session.get('selected_designer_id', 'Rahul_mis')).strip()

    key = request.session.get('session_key')
    user = User.objects.get(u_ID=key)

    if key:
        all_messages = Message.objects.filter(user=user).order_by('designer')
        des = Designer.objects.get(d_ID=q)
        chat_messages = Message.objects.filter(user=user, designer=des)
        distinct_users = []
        messages = []
        for message in all_messages:
            if message.designer not in distinct_users:
                distinct_users.append(message.designer)
                messages.append(message)
        if request.method == 'POST':

            message = request.POST.get('message', '')
            if message:
                chat_message = Message() 
                chat_message.user = user
                chat_message.designer = des
                if isinstance(user, User):
                    chat_message.user_message = message
                elif isinstance(user, Designer):
                    chat_message.designer_message = message
                chat_message.save()
                request.session['selected_designer_id'] = q
                return redirect('user_chats')
        else:
            return render(request, 'fn_app/user/chat.html', {'msg': messages, 'user':user,'receiver': des, 'chat_messages': chat_messages})
        return render(request, 'fn_app/user/chat.html', {'msg': messages, 'user':user,'receiver': des, 'chat_messages': chat_messages})
    else:
        return redirect('user_registration')


