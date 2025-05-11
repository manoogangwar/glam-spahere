from django.urls import path,include
from.import views,user_views,designer_views
urlpatterns=[
    path("", views.home , name="home"),
    path("contact_us/", views.contactus, name="contact_us"),
    path("about/", views.about, name="about"),
    path("feedback/", views.feedback, name="feedback"),
    path("user_login/", user_views.user_login, name="user_login"),
    path("user_reg/", user_views.user_reg, name="user_registration"),
    path("d_register/", designer_views.d_register, name="d_register"),
    path("events/", views.event_update, name="events"),
    path("more_feedback/", views.more_feedback, name="more_feedback"),
    path("user_home/", user_views.user_home,name='user_home'),
    path("designer_home/", designer_views.designer_home,name='designer_home'),
    path("designer_login/",designer_views.designer_login, name='designer_login'),
    path('user_edit_home/', user_views.user_edit_home,name='user_edit_home'),
    path('designer_edit_home/', designer_views.designer_edit_home,name='designer_edit_home'),
    path('add_job/', designer_views.add_job,name='add_job'),
    path('logout/',user_views.logout,name='logout'),
    path("d_workscollection/",designer_views.d_works_coll,name="designer_works_collection"), #for adding work collection
    path("designer/<str:id>/",views.work_detail,name="work_details"),
    path("post_tips/", designer_views.post_tips, name="post_tips"),
    path("news/",views.news_update,name='news'),
    path('job_request/',user_views.job_request,name='job_request'),
    # path("compose/",user_views.compose, name="compose" ), #for user messages
    # path("dcompose/",designer_views.compose, name='compose'),
    # path("checkId/",designer_views.checkId,name="checkId"), #check id for designer
    # path("checkId2/",user_views.checkId2,name="checkId2"), #checkid for user
    path('collections/', designer_views.all_collections, name='collections'),
    path('user_chats/',views.userchat,name='user_chats'),
  
    path('designer_messages/', views.designer_messages, name='designer_messages'),
    path('chat/<str:id>/', views.chat, name='chat'),
    path('send_message/<str:id>/', views.send_message, name='send_message')

]