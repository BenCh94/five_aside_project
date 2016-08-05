from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
# import logging
from django.contrib.auth.decorators import login_required
# log = logging.getLogger(__name__)


def post_list(request):
    # log.info("Handling post_list %s request", request.method)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_list_by_views(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')
    return render(request, "blogposts.html", {'posts': posts})


def post_details(request, id):
    # log.info("Handling post_details %s request", request.method)
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


@login_required(login_url='/login/')
def new_post(request):
    # log.info("Handling new_post %s request", request.method)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})


def edit_post(request, id):
    # log.info("Handling edit_post %s request", request.method)
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {"form": form})

