from django.db import models
from django.utils import timezone
# Create your models here.
#news model
class News(models.Model):
    news_content=models.TextField()
    photo=models.FileField(max_length=100, upload_to='fn_app/news_photo', default="")
    news_headline=models.CharField(max_length=100)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.news_headline




# tips and tricks model
class TipsTricks(models.Model):
     designer = models.ForeignKey('Designer', on_delete=models.DO_NOTHING)   
     content=models.TextField(max_length=1000)
     date=models.DateField(default=timezone.now)
     def __str__(self):
        return self.designer.d_name

#designerwork

class DesignerWork(models.Model):
    designer = models.ForeignKey('Designer', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    year= models.CharField(max_length=4)
    client=models.CharField(max_length=20, null=True)
    photo=models.FileField(max_length=100, upload_to='fn_app/designer_pics', default="")
    def __str__(self):
        return self.designer.d_name
# job model
class Job(models.Model):
    designer=models.ForeignKey('Designer',on_delete=models.DO_NOTHING)
    designation=models.CharField(max_length=20)
    seats_available=models.CharField(max_length=50)
    mailing_link=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=30)
    work_profile=models.CharField(max_length=100)
    min_qual=models.CharField(max_length=40)
    job_location=models.CharField(max_length=30)
    age_req=models.CharField(max_length=2)
    last_date=models.DateField(default=timezone.now)
    salary_pkg=models.CharField(max_length=6)
    date_posted=models.DateField(default=timezone.now)
    def __str__(self):
        return self.designer.d_name

# designer model
class Designer(models.Model):
    d_pic = models.FileField(max_length=100, upload_to='Designers/', default="")
    d_ID=models.CharField(max_length=20,primary_key=True)
    d_password=models.CharField(max_length=20)
    d_name=models.CharField(max_length=40)
    d_mail=models.EmailField(unique=True)
    d_phone=models.CharField(max_length=11)
    d_qualification=models.CharField(max_length=20)
    d_state=models.CharField(max_length=20)
    d_city=models.CharField(max_length=20)
    designer = models.BooleanField(default=True)
    d_gender=models.CharField(max_length=6)
    d_skills=models.CharField(max_length=50)
    d_about=models.TextField()
    date=models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return self.d_name

# feedback model

class FeedBack(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    remarks = models.TextField(null=True)
    rating = models.CharField(max_length=2) 
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name


    #contact model
class Contact(models.Model):
    name= models.CharField(max_length=45)
    email = models.EmailField(max_length=45) 
    phone=models.CharField(max_length=10)  
    question=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

#event model
class Event(models.Model):
    event_name=models.CharField(max_length=60,primary_key=True)
    event_venue=models.CharField(max_length=80, default="Auditorium")
    event_date=models.DateField(default=timezone.now)
    event_description=models.TextField()
    evnt_gallery=models.FileField(max_length=100, upload_to='fn_app/event_gallery', default="")
    def __str__(self):
        return self.event_name

# user class for user registration and login
class User(models.Model):
    u_pic = models.FileField(max_length=100, upload_to='Users/', default="")
    u_ID=models.CharField(max_length=20,primary_key=True)
    u_password=models.CharField(max_length=20)
    u_name=models.CharField(max_length=40)
    u_mail=models.EmailField(unique=True)
    u_gender=models.CharField(max_length=6)
    u_phone=models.CharField(max_length=11)
    u_address=models.TextField()
    user = models.BooleanField(default=True)
    u_city=models.CharField(max_length=20)
    u_state=models.CharField(max_length=20)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.u_name
    
#message model
class Message(models.Model):
    user=models.ForeignKey(User,  on_delete=models.DO_NOTHING)
    designer=models.ForeignKey(Designer, on_delete=models.DO_NOTHING)
    user_message=models.CharField(max_length=250, null=True, blank=True)
    designer_message=models.CharField(max_length=250, null=True, blank=True)
    date=models.DateField(default=timezone.now)
    # def __str__(self):
    #     return self.sender_id
