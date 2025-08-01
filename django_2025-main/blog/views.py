from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
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
    categories= Category.objects.all()
    return render(request,
                  'blog/detail.html',
                  context={'post2':post1111,'categories':categories})

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