from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from .models import Category
# Create your views here.

#함수 생성
def index(request):
    #db에서 query - select * from post
    posts1111 = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request,
                  'blog/index.html',
                  context={'posts':posts1111, 'categories':categories}
                 )

def category(request, slug):
    categories = Category.objects.all()
    if slug=='none':
        posts1111=Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        posts1111=Post.objects.filter(category=category)
        #db에서 query - select * from post
    return render(request,
                  'blog/index.html',
                  context={'posts':posts1111, 'categories':categories}
                 )

def detail(request, pk):
    post1111 = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post1111)
    categories= Category.objects.all()
    commentform=CommentForm()
    return render(request,
                  'blog/detail.html',
                  context={'post2':post1111,'categories':categories,'comments':comments, 'commentform':commentform})

def create(request):
    categories= Category.objects.all()
    if request.method == "POST":
        #제출
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post1=postform.save(commit=False)
        
            post1.save()
            return redirect('/blog/')
            
    else: 
        postform = PostForm()

    return render(request, template_name='blog/postform.html', context={'postform':postform,'categories':categories})

def createfake(request):
    post = Post()
    post.title="새싹 용산구"
    post.content="나진상가 3층"
    post.save()
    return redirect('/blog/')

def delete(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

def update(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        postform=PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('/blog/')
    else:
        postform=PostForm(instance=post) 
    return render(request, template_name="blog/postupdateform.html",context={'postform':postform})

def createComment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        #제출
        commentform = CommentForm(request.POST, request.FILES)
        if commentform.is_valid():
            comment1=commentform.save(commit=False)
            comment1.post = post
            comment1.save()
            return redirect(f'/blog/{post.pk}/')
            
    else: 
        commentform = CommentForm()

    return render(request, template_name='blog/commentform.html', context={'commentform':commentform})

def updateComment(request,pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        commentform=CommentForm(request.POST, request.FILES, instance=comment)
        if commentform.is_valid():
            commentform.save()
            return redirect(f'/blog/{comment.post.pk}/')
    else:
        commentform=CommentForm(instance=comment) 
    return render(request, template_name="blog/commentupdateform.html",context={'commentform':commentform})

def deleteComment(request,pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/')