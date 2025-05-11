from django.contrib import admin
from .models import FeedBack,Contact,Event,Designer,DesignerWork,News,User,Job,TipsTricks,Message,News
# Register your models here.
class Feedback_Admin(admin.ModelAdmin):
    list_display = ('name','email','remarks', 'rating')
class ContactUs_Admin(admin.ModelAdmin):
    list_display=('name', 'email','phone')
class Designer_Admin(admin.ModelAdmin):
    list_display=('d_ID','d_name','d_mail', 'd_phone','d_city','d_qualification')
    list_filter=('d_city','d_qualification',)
class DesignerWork_Admin(admin.ModelAdmin):
    list_display=('designer','title','year','client')
    

class User_Admin(admin.ModelAdmin):
    list_display=('u_ID','u_name','u_mail', 'u_phone','u_city')
    search_fields=('city',)


admin.site.register(FeedBack,Feedback_Admin)
admin.site.register(Contact,ContactUs_Admin)
admin.site.register(Event)
admin.site.register(Designer,Designer_Admin)
admin.site.register(DesignerWork,DesignerWork_Admin)
admin.site.register(User,User_Admin)
admin.site.register(Job)
admin.site.register(TipsTricks)
admin.site.register(Message)
admin.site.register(News)

admin.site.site_header = "Glam Sphere Admin Dashboard"
admin.site.site_title = "Glam Sphere Admin Portal"
admin.site.index_title = "Welcome to Glam Sphere Admin Portal"
