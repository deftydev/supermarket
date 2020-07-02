from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.utils.decorators import method_decorator
from .decorators import teacher_required

class HomePageView(LoginRequiredMixin,ListView):
    template_name='products/home.html'
    model = Product
    context_object_name='products'

    def get_queryset(self):
        products = super().get_queryset()
        return products



@method_decorator([login_required, teacher_required], name='dispatch')
class ProductCreateView(CreateView):
    model=Product
    template_name='products/create.html'
    fields=['contact','number','description','image','title']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.save()
        return redirect('home')

@method_decorator([login_required, teacher_required], name='dispatch')
class ProductUpdateView(UpdateView):
    model=Product
    template_name='products/update.html'
    fields=['contact','number','description','image','title']
    def form_valid(self,form):
        instance=form.save()
        return redirect('/',instance.pk)


@method_decorator([login_required, teacher_required], name='dispatch')
class ProductDeleteView(DeleteView):
    model=Product
    template_name='products/delete.html'
    fields=['contact','number','description','image','title']
    success_url='/'




@login_required(login_url="/accounts/signup")
def detail(request,product_id):
    product=get_object_or_404(Product, pk=product_id)
    return render(request,'products/detail.html',{'product':product})


@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
    if request.method=="POST":
        product=get_object_or_404(Product , pk=product_id)
        product.votes_total +=1
        product.save()
        return redirect('/products/' + str(product.id))
