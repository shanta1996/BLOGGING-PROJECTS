from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def view_blogs(request):
    blogs=Blogging.objects.all()
    recentpost=Blogging.objects.all()[::-1]
    category=Category.objects.all()
    if request.method=="GET":
        search=request.GET.get('search')
        if search!=None:
            blogs=Blogging.objects.filter(title__icontains=search)

    context={
        'blogs':blogs,
        'recentpost':recentpost,
        'category':category
    }
    return render(request,'bloggingapi/home.html',context)




def post_blogs(request):
    if request.method=="POST":
        form=BloggingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Blog added successfully.')
            return redirect('/addblogs')
        else:
            messages.add_message(request,messages.ERROR,'Failed to add Blog.')
            return render(request,'bloggingapi/addblogs.html',{'form':form})
    context={
        'form':BloggingForm 
    }
    return render(request,'bloggingapi/addblogs.html',context)



# def update_blog(request,blog_id):
#     instance=Blogging.objects.get(id=blog_id)

#     if request.method=='POST':
#         form=BloggingForm(request.POST,request.FILES,instance=instance)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request,messages.SUCCESS,'Blog updated successfully.')
#             return redirect('/')
        
#         else:
#             messages.add_message(request,messages.ERROR,'Failed to update Blog.')
#             return render(request,'bloggingapi/updateblogs.html',{'form':form})
#     context={
#         'form':BloggingForm(instance=instance)
#     }
#     return render(request,'bloggingapi/updateblogs.html',context)



def delete_blog(request,blog_id):
    blog=Blogging.objects.get(id=blog_id)
    blog.delete()
    messages.add_message(request,messages.SUCCESS,'Blog deleted successfully.')
    return redirect('/')


# ALL BLOGS 
def all_blogs(request):
    allblogs=Blogging.objects.all()
    context={
        'allblogs':allblogs,
        
    }
    return render(request,'bloggingapi/all-blog.html',context)

def update_allblogs(request,allblog_id):
    instance=Blogging.objects.get(id=allblog_id)

    if request.method=='POST':
        form=BloggingForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Blog updated successfully.')
            return redirect('/')
        
        else:
            messages.add_message(request,messages.ERROR,'Failed to update Blog.')
            return render(request,'bloggingapi/all-blogupdate.html',{'form':form})
    context={
        'form':BloggingForm(instance=instance)
    }
    return render(request,'bloggingapi/all-blogupdate.html',context)



# Category
def post_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category added successfully.')
            return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,'Failed to add Category')
            return render(request,'bloggingapi/addcategory.html',{'form':form})
    context={
        'form':CategoryForm
    }
    return render(request,'bloggingapi/addcategory.html',context)



# def update_category(request,category_id):
#     instance=Category.objects.get(id=category_id)

#     if request.method=='POST':
#         form=CategoryForm(request.POST,instance=instance)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request,messages.SUCCESS,'Category updated successfully.')
#             return redirect('/category')
        
#         else:
#             messages.add_message(request,messages.ERROR,'Failed to update Category.')
#             return render(request,'bloggingapi/updatecategory.html',{'form':form})
#     context={
#         'form':CategoryForm(instance=instance)
#     }
#     return render(request,'bloggingapi/updatecategory.html',context)


# def delete_category(request,category_id):
#     category=Category.objects.get(id=category_id)
#     category.delete()
#     messages.add_message(request,messages.SUCCESS,'Blog deleted successfully.')
#     return redirect('/category')

def read_category(request,read_id):
    r_category=Category.objects.get(id=read_id)
    blogs=Blogging.objects.filter(category=r_category)
    context={
        'r_category':r_category,
        'blogs':blogs
    }
    return render(request,'bloggingapi/read-category.html',context)


# view single blog 

def single_blog(request,single_id):
    single_blog=Blogging.objects.filter(id=single_id)
    context={
        'single_blog':single_blog,
        
    }
    return render(request,'bloggingapi/single-blog.html',context)



# def comment(request):
#     if request.method=='POST':


def addingblogs(request):
    mess=''
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        # file=request.POST['file']
        blogs=Blogging(title=title,content=content)
        blogs.save()
        mess='added'
        return redirect('/')
    return render(request,'bloggingapi/addingblogs.html',{'mess':mess})


