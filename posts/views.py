from django.shortcuts import render, redirect, get_object_or_404

from ProjectA.settings import EMAIL_HOST_USER
from posts.models import User, Posts, Posts2, RegUser
from .forms import CreateUser
from django.core.mail import send_mail, EmailMessage


# Create your views here.

def index(request):
    return render(request, 'posts/index.html')


def about(request):
    return render(request, 'posts/about.html')


def nurs(request):
    return render(request, 'posts/nurs.html')


def register(request):
    return render(request, 'posts/register.html')


def contact(request):
    return render(request, 'posts/contactus.html')


def mainpage(request):
    return render(request, 'posts/mainpage.html')


def home(request):
    return render(request, 'posts/home.html')


def someinfo(request):
    return render(request, 'posts/someinfo.html')


def u_comment(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'posts/u_comment.html', context)


def create(request):
    user = User(username=request.POST['username'], commentary=request.POST['commentary'])
    user.save()
    return redirect('/')


def edit(request, id):
    users = User.objects.get(id=id)
    context = {'users': users}
    return render(request, 'posts/edit.html', context)


def update(request, id):
    user = User.objects.get(id=id)
    user.username = request.POST['username']
    user.commentary = request.POST['commentary']
    user.save()
    return redirect('/')


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')


def create1(request):
    sposts = Posts(title=request.POST['title'], content=request.POST['content'], author=request.POST['author'],
                   describe=request.POST['describe'], email=request.POST['email'])
    sposts.save()
    return redirect('/')


def edit1(request, id):
    spostes = Posts.objects.get(id=id)
    context = {'spotses': spostes}
    return render(request, 'posts/edit1.html', context)


def update1(request, id):
    sposts = Posts.objects.get(id=id)
    sposts.title = request.POST['title']
    sposts.content = request.POST['content']
    sposts.author = request.POST['author']
    sposts.describe = request.POST['describe']
    sposts.email = request.POST['email']
    sposts.save()
    return redirect('/')


def delete1(request, id):
    spost = Posts.objects.get(id=id)
    spost.delete()
    return redirect('/')


def lec9(request):
    return render(request, 'posts/9lec.html')


def show_post(request, post_slug):
    post = get_object_or_404(Posts2, slug=post_slug)
    context = {'post': post}
    return render(request, 'posts/post.html', context=context)


def createuser(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('create_user')
            except:
                form.add_error(None, 'Failed attempt to create user')
    else:
        form = CreateUser()
    send_mail("The first message", "My content",
              "200103158@stu.sdu.edu.kz", ["200103158@stu.sdu.edu.kz", "miras.isabekov7@gmail.com"],
              fail_silently=False,
              html_message="<h2><i><span style='color:green'>Д</span>обро...пожаловать!</i></h2><img src='https://avatars.mds.yandex.net/i?id=cb667720a1a0f1716f71e3e2038d914b-5309177-images-thumbs&n=13'>")
    return render(request, 'posts/registration.html', {'form': form})

def bonus_main(request):
    return render(request, 'bonus/main_site.html')
