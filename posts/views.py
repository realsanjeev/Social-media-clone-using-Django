import os
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from userprofile.models import Profile, FollowerCount
from posts.models import Posts, LikePost

# Create your views here.
@login_required(login_url="/login")
def home(request):
    context = dict()
    template_files = os.path.join("posts", "home.html")
    user_profile = Profile.objects.filter(user=request.user).first()
    post_objs = Posts.objects.all()
    
    context["user_profile"] = user_profile
    context["posts"] = post_objs
    return render(request, template_files, context)

@login_required(login_url="login")
def posts(request):
    context = dict()
    template_files = os.path.join("posts", "home.html")
    user_profile = Profile.objects.get(user=request.user)
    post_objs = Posts.objects.all()
    
    print('----------------------',post_objs)
    context["user_profile"] = user_profile
    context["posts"] = post_objs
    return render(request, template_files, context)

@login_required(login_url='login')
def upload_view(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {"user_profile": user_profile}
    template_files = os.path.join('posts', 'upload.html')

    if request.method == 'POST':
        post_pics = request.FILES.get('post_pics')
        caption = request.POST.get('caption')

        if post_pics is None:
            context["message"] = "Please upload the Image to post"
            return render(request, template_files, context)  # Corrected this line to return the response.

        else:
            new_post_obj = Posts(user=request.user.username, post_img=post_pics, caption=caption)
            new_post_obj.save()
            return redirect('/')

    return render(request, template_files, context)

@login_required(login_url='login')
def like_post_view(request):
    username = request.user.username
    post_id = request.GET.get("post_id")
    post_obj = Posts.objects.get(id=post_id)
    is_liked_before = LikePost.objects.filter(username=username, post_id=post_id).exists()

    if not is_liked_before:
        like_post = LikePost(username=username, post_id=post_id)
        like_post.save()
        post_obj.likes += 1
        post_obj.save()
        return redirect('/')
    else:
        post_obj.likes -= 1
        LikePost.objects.filter(username=username, post_id=post_id).delete()
        post_obj.save()

    return redirect('/')

def user_view(request, username):
    template_file = "posts/user.html"
    error_file = "user/notFound.html"
    context = {}
    
    if request.user.username == username:
        return redirect("/profile")

    try:
        user_main = User.objects.get(username=username)
        user_profile = Profile.objects.filter(user=user_main).first()
        post_objs = Posts.objects.filter(user=username)
        is_following = FollowerCount.objects.filter(follower=request.user.username, user=username).exists()
        context["num_following"] = FollowerCount.objects.filter(follower=username).count()
        context["num_follower"] = FollowerCount.objects.filter(user=username).count()
        print('-------------',is_following)
        context["is_following"] = is_following
        context["user"] = user_main
        context["user_profile"] = user_profile
        context["posts"] = post_objs
        return render(request, template_file, context)
    
    except User.DoesNotExist:
        err_msg = {"message": f"user/{username} not found"}
        return render(request, error_file, err_msg)
    
    except Profile.DoesNotExist:
        err_msg = {"message": f"Profile not found for {username}"}
        return render(request, error_file, err_msg)

