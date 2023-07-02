import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from userprofile.models import Profile
from posts.models import Posts

# Create your views here.
@login_required(login_url="/login")
def home(request):
    template_files = os.path.join("posts", "home.html")
    user_profile = Profile.objects.create(user=request.user, id_user=request.user.id)
    context = {"user_profile": user_profile}
    return render(request, template_files, context)

@login_required(login_url="login")
def posts(request):
    template_files = os.path.join("posts", "home.html")
    user_profile = Profile.objects.create(user=request.user, id_user=request.user.id)
    post_objs = Posts.objects.get()
    print(post_objs)
    posts = {"posts": post_objs}
    context = {"user_profile": user_profile}
    return render(request, template_files, posts, context)

@login_required(login_url='login')
def upload_view(request):
    user_profile = Profile.objects.create(user=request.user, id_user=request.user.id)
    context = {"user_profile": user_profile}
    template_files = os.path.join('posts',  'upload.html')
    if request.method == 'POST':
        post_pics = request.FILES.get('post_pics')
        caption = request.POST.get('caption')
        if post_pics is None:
            context["message"] = "Please upload the Image to post"
            render(request, template_files, context)
        else:
            new_post_objs = Posts(user=request.user.username, 
                                  post_img=post_pics, caption=caption)
            new_post_objs.save()
            redirect('/')
        pass
    return render(request, template_files, context)