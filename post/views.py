from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse , Http404 
from .models import Post , comments
from .forms import commentsForm , post_uploadform
from django.views import View
from django.views.generic.edit import CreateView 
from django.views.generic import DetailView
from .forms import loginForm , Login_pageForm
from django.contrib.auth import authenticate , login ,logout

# Create your views here.
# class sessionreadme(DetailView):
#     model = Post
#     template_name = "post.html"
#     context_object_name = 'post'
#     slug_field = 'slug'
#     slug_url_kwarg = 'post_slag'
    
class addreadlater(View):
    def post(self, request):
        selected_id = request.POST["readlater_id"]
        readme_later_id = Post.objects.get(pk=selected_id)
        request.session["readme_later"] = readme_later_id.slug
        slag = request.session["readme_later"]
        print("Session readlater_id:",request.session["readme_later"])
        return redirect("post" , post_slag = slag)
class Register(View):
    def post(self,request):
        form = loginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # encrypt password
            user.save()
            login(request, user)  # auto login after registration
            return redirect("home")  # change 'home' to your homepage URL name
        else:
            form = loginForm()
        # Always return a response
        return render(request, 'post/register.html', {'form': form})
    def get(self,request):
        form = loginForm()
        return render(request, 'post/register.html', {'form': form})
class Login(View):
    def post(self, request):
        form = Login_pageForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect after login
            else:
                form.add_error(None, "Invalid username or password.")
        # Always return a response
        return render(request, 'post/login.html', {'form': form})
    def get(self,request):
        form = Login_pageForm()
        return render(request, 'post/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')

def home_page(request):
    posts = Post.objects.order_by('-date')[:3]
    readme_id = request.session.get("readme_later")
    
    post_slug = None
    if readme_id:
        try:
            
                
                post_slug = readme_id
        except:
            post_slug = None
    return render(request,"post/home.html",{"posts":posts ,"session_slug": post_slug})

# def post_page(request):
#     posts = Post.objects.all()
#     return render(request,"post/post_page.html" , {"posts":posts})
class post_page(CreateView):
    model = Post
    form_class = post_uploadform
    template_name = "post/post_page.html"
    success_url = '/post' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    
# class post_page(View):
#     def post(self , request ):
#         upload = post_uploadform(request.POST , request.FILES)
#         posts = Post.objects.all()
#         if upload.is_valid():
#             enter_post = posts(image= request.FILES["user_upload"])
#             enter_post.save()
#         return render(request,"post/post_page.html" , {"posts":posts})
#     def get(self , request):
#         upload = post_uploadform()
#         posts = Post.objects.all()
#         return render(request,"post/post_page.html" , {"posts":posts ,"upload_post": upload})
    

# def post(request , slag):
#     posts = get_object_or_404(Post , slug = slag)
#     slags = Post.objects.values_list("slug")
#     comments = commentsForm()
        
#     return render(request , "post/post.html",{ "slags":slag ,"posts":posts , "comments" : comments} )

class post(View):
    def post(self , request , post_slag):
        posts = get_object_or_404(Post , slug = post_slag)
        slags = Post.objects.values_list("slug")
        commentsform = commentsForm(request.POST)
 
        if commentsform.is_valid():
            comment_instance = commentsform.save(commit=False)
            comment_instance.title = posts.title
            commentsform.save()
            post_title = posts.title
            list_comments = comments.objects.filter(title = post_title)
            return render(request , "post/post.html",{ 
                                                  "slags":slags ,
                                                  "posts":posts ,
                                                  "comments" : commentsform,
                                                  "list_comments": list_comments
                                                } )
    def get(self, request , post_slag):
        posts = get_object_or_404(Post , slug = post_slag)
        
        slags = Post.objects.values_list("slug")
        commentsform = commentsForm()
        post_title = posts.title
        list_comments = comments.objects.filter(title = post_title)
        return render(request , "post/post.html",{ 
                                                  "slags":slags ,
                                                  "posts":posts ,
                                                  "comments" : commentsform,
                                                   "list_comments": list_comments,
                                                   
                                                } )