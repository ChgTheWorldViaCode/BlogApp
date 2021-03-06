from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request,'blog/post_list.html',stuff_for_frontend)

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    stuff_for_frontend = {'post' : post} 
    return render(request, 'blog/post_detail.html',stuff_for_frontend) 

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)    
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:    
        form = PostForm()
        stuff_for_frontend = {'form': form}
        return render(request,'blog/post_edit.html',stuff_for_frontend)

@login_required
def post_edit(request, pk):
    # Get DB record from Post model via Primay Key
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        #Updating an Existing Form (for existing post)
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #Updating an Existing Form (for existing post)
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post': post}
        return render(request,'blog/post_edit.html',stuff_for_frontend)

@login_required
def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')
            

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-date_created')
    stuff_for_frontend = {'posts': posts}
    return render(request,'blog/post_draft_list.html',stuff_for_frontend)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = post   
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:    
        form = CommentForm()
        stuff_for_frontend = {'form': form, 'post': post}
        return render(request,'blog/add_comment_to_post.html',stuff_for_frontend)


@login_required
def comment_remove(request, pk):        
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()        
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_approve(request, pk):        
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()        
    return redirect('post_detail', pk=comment.post.pk)