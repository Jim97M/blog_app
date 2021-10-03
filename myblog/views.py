from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def post_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 10)
    print(request.GET)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "myblog/homepage.html", context={'posts':posts})

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    emailform = EmailForm()
    comments = Comment.objects.filter(post=post)
    post_tags = Post.tags.all()
    if request.method == 'POST':
        print(request.POST)
        emailform = EmailForm(request.POST)
        if emailform.is_valid():
            cd = emailform.cleaned_data
            print(cd)
            name = cd['name']
            to = cd['to']
            message = cd['comment']
            subject = f"Shared post by{name}"
            senders_email = settings.EMAIL_HOST_USER
            send_mail(
                subject,
                message,
                senders_email,
                [to]
            )
        return HttpResponseRedirect(reverse('myblog:detailview', args=[pk]))
    return render(request, "myblog/detail.html", 
           {'post':post,
           'emailform':emailform})