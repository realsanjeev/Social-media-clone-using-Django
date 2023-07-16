import os
from itertools import chain
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from userprofile.models import Profile, FollowerCount
from posts.models import Posts, LikePost, CommentPost

# using class for views
#  using class for templating
# class SearchResultsView(ListView):
#     model = Profile
#     template_name = 'posts/search.html'
#     context_object_name = 'profiles'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Profile.objects.filter(
#             Q(user__username__icontains=query) |
#             Q(user__first_name__icontains=query) |
#             Q(user__last_name__icontains=query)
#         )
#         return object_list


# Create your views here.
@login_required(login_url="/login")
def home(request):
    context = dict()
    template_files = os.path.join("posts", "home.html")
    user_profile = Profile.objects.filter(user=request.user).first()
    following_lst = list()
    post_feed = list()
    following_obj = FollowerCount.objects.filter(follower=request.user.username)
    if following_obj is None:
        following_lst = []
        post_feed = Posts.objects.all()
    else:
        for followed_user in following_obj:
            following_lst.append(followed_user.user)
        for followed_user in following_lst:
            posts_objs = Posts.objects.filter(user=followed_user)
            post_feed.append(posts_objs)
        post_feed = list(chain(*post_feed))
        if not len(post_feed):
            post_feed = Posts.objects.all()
    context["user_profile"] = user_profile
    context["posts"] = post_feed
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

def search_user(request):
    template_file = os.path.join("posts", "search.html")
    context = dict()
    context["user_profile"] = Profile.objects.filter(user=request.user).first()
    if request.method == "GET":
        query = request.GET.get('q')
        context["query"] = query
        context["object_list"] = Profile.objects.filter(
            Q(user__username__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        )
    return render(request, template_file, context)

@login_required(login_url='login')
def explore_view(request):
    template_file = os.path.join('posts', 'explore.html')
    context = dict()
    context['user_profile'] = Profile.objects.filter(user=request.user).first()
    context['posts'] = Posts.objects.filter(user=request.user.username)
    return render(request, template_file, context)

@login_required(login_url='login')
def notification_view(request):
    template_file = os.path.join('posts','notification.html')
    context = {}
    context['user_profile'] = Profile.objects.filter(user=request.user).first()
    followed_users = FollowerCount.objects.filter(follower=request.user.username)
    context['unfollowed_profiles'] = Profile.objects.exclude(Q(user__username__in=followed_users.values('user')) | Q(user__username=request.user.username))
    print('*'*23, context['unfollowed_profiles'] )
    return render(request, template_file, context)

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

@login_required(login_url='login')
def comment_view(request):
    username = request.user.username
    post_id = request.GET.get("post_id")
    if request.method=="POST":
        new_comment = request.POST.get('comment')
        comment_obj = CommentPost(username=username, post_id=post_id, comment=new_comment)
        comment_obj.save()
    return HttpResponse('Coment box is working')