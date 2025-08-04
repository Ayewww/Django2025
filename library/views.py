from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

#함수 생성
def index(request):
    #db에서 query - select * from post
    posts1111 = Post.objects.all().order_by('-pk')
    return render(request,
                  'library/index.html',
                  context={'posts':posts1111}
                 )
def detail(request, pk):
    post1111 = Post.objects.get(pk=pk)
    return render(request,
                  'library/detail.html',
                  context={'post2':post1111})

def create(request):
    if request.method == "POST":
        #제출
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post1=postform.save(commit=False)
            post1.title = post1.title + "입니다"
            post1.save()
            return redirect('/library/')
            
    else: 
        postform = PostForm()

    return render(request, template_name='library/postform.html', context={'postform':postform})

def createfake(request):
    post = Post()
    post.title="새싹 용산구"
    post.content="나진상가 3층"
    post.save()
    return redirect('/library/')