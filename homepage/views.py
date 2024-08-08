from django.shortcuts import render, redirect
from .models import Watches, WatchesUpload,Wishlist
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout

def Home(request):
    watches = Watches.objects.all()
    context = {'watches_t': watches}
    return render(request, "home.html", context)

def About(request):
    return render(request, "about.html")


@login_required(login_url="/login")
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            return redirect('home')
    else:
        form = UploadForm()

    return render(request, "WatchUploads.html", {'form': form})



def login_page(request):

    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=user_name,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request,"login.html",{'form':form})

    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form})

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request,"signup.html",{'form':form})



def logout_user(request):
    logout(request)
    return redirect('home')


from django.shortcuts import get_object_or_404
def show_product(request,id):
    product = get_object_or_404(WatchesUpload,id=id)
    return render(request,'product.html',{"product":product})


from django.shortcuts import get_object_or_404, redirect

def addtowish(request,id):
    user = request.user
    product = WatchesUpload.objects.get(id=id)
    print("This is the user",type(user),user.username,user.id)
    obj1 = Wishlist(user=user)
    obj1.save()
    obj1.user.add()
    obj1.products.add(product)
    obj1.save()
    return redirect('home')
