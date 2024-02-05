from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from main.forms import RegisterForm, PostForm, ReplyForm
from .models import Post

# Create your views here.
@login_required(login_url = "/login")
def home(request) :
    posts = Post.objects.all().order_by("-created_at")
    if request.method == "POST" :
        post_id = request.POST.get("post-id")
        user_id_ban = request.POST.get("user-id-ban")
        user_id_unban = request.POST.get("user-id-unban")
        if post_id :
            post = posts.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")) :
                posts.pop(post)
                post.delete()
        
        if user_id_ban :
            user = User.objects.filter(id=user_id_ban).first()
            if user and request.user.is_staff :
                try :
                    group = Group.objects.get(name="default")
                    group.user_set.remove(user)
                except :
                    pass

                try :
                    group = Group.objects.get(name="mod")
                    group.user_set.remove(user)
                except :
                    pass
        elif user_id_unban :
            user = User.objects.get(id=user_id_unban)
            if user and request.user.is_staff :
                try :
                    group = Group.objects.get(name="default")
                    group.user_set.add(user)
                except :
                    pass
        # if parent_id :
        #     replyform = ReplyForm(request.POST)
        #     if replyform.is_valid() :
        #         post = replyform.save(commit=False)
        #         post.replyTo = mainPosts.get(id=parent_id)
        #         post.commentAuthor = request.user
        #         post.save()
        #         return redirect("/home")
    return render(request, "main/home.html", {"posts" : posts})

def sign_up(request) :
    if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            return redirect('/home')
    else :
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"form" : form})

@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=False)
def create_post(request) :
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else :
        form = PostForm()
    return render(request, "main/create_post.html", {"form" : form})

@login_required(login_url="/login")
def my_profile(request) :
    posts = Post.objects.filter(author_id = request.user.id)
    return render(request, "main/my_profile.html", {"posts" : posts})

def profile_view(request, id) :
    posts = Post.objects.filter(author_id = id)
    viewing = User.objects.filter(id = id).first()
    return render(request, "main/profile.html", {"posts" : posts, "viewing" : viewing})

@login_required(login_url = "/login")
def delete_user(request) :
    user = User.objects.filter(id = request.user.id)
    logout(request)
    user.delete()
    return redirect("/login")

@login_required(login_url = "/login")
def view_post(request, post_id) :
    post = Post.objects.get(id = post_id)
    replies = post.replies.all()
    if request.method == "POST" :
        form = ReplyForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit=False)
            comment.commentAuthor = request.user
            comment.replyTo = post
    else :
        form = ReplyForm()
    return render(request, "main/view_post.html", {"post" : post, "form" : form, "replies" : replies})


