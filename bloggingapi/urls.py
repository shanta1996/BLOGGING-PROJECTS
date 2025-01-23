from django.urls import path
from .views import *

urlpatterns = [
    path('',view_blogs),
    path('addblogs/',post_blogs),
    # path('updateblogs/<int:blog_id>',update_blog),
    path('deleteblog/<int:blog_id>',delete_blog),
    path('allblogs/',all_blogs),
    path('all-blog-update/<int:allblog_id>',update_allblogs),
    path('addcategory/',post_category),
    # path('updatecategory/<int:category_id>',update_category), 
    # path('deletecategory/<int:category_id>',delete_category),
    path('singleblog/<int:single_id>',single_blog),
    path('readcategory/<int:read_id>',read_category),
    path('addingblogs/',addingblogs),
    
]
