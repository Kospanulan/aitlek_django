from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.form import LoginForm, PostCreateForm
from blog.models import Post


def login_view(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)

                return redirect('posts')
            return HttpResponse("Вы не залогинелись")

    elif request.method == 'GET':
        form = LoginForm()
        return render(
            request=request,
            template_name="blog/login_page.html",
            context={"title": "Login", "form": form}
        )


def logout_view(request):
    logout(request)
    return redirect('home')


# вьюшки
def home_page(request):
    return HttpResponse("Общедоступная страница")


@login_required
def get_posts(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="blog/posts_page.html",
        context={
            "title": "Все Посты",
            "posts": posts
        }
    )


def post_by_id(request, post_id):
    post = Post.objects.get(id=post_id)
    return HttpResponse(f"<p>post_id: {post.id}</p>"
                        f"<h1> {post.title}</h1>"
                        f"<p>{post.text}</p>")


# @permission_required(('blog.add_post', 'blog.view_post'))
@permission_required('blog.add_post')
def create_post(request):
    if request.method == 'POST':

        form = PostCreateForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            print("Current user:", request.user)

            new_post.author = request.user
            new_post.save()

            cd = form.cleaned_data
            print(cd)

            return redirect('posts')

    else:
        form = PostCreateForm()

    return render(
        request=request,
        template_name="blog/create_post.html",
        context={'form': form, 'title': "Create Post"}
    )
