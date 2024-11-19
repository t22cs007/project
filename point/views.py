from django.shortcuts import render, resolve_url, redirect
# from .forms import ContributionForm, PostForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from .models import Point
from .forms import ContributionForm
from django.contrib.auth.decorators import login_required

# from .models import Author

class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "point/point_top.html"

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = False
    
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class PostUpload(OnlyYouMixin, generic.CreateView):
    template_name = 'point/post_upload.html'
    form_class = Point

    def form_valid(self, form):
        form.instance.user = self.request.user  # 修正箇所
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('POINT:Index')

class Post(generic.DetailView):
    template_name = 'point/post.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "point_create.html"
    fields = ['content']
    success_url = reverse_lazy('point:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
@login_required
def create(request):
    if request.method == "POST":
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.user = request.user
            contribution.save()
            return redirect('point:point_success')  # 成功ページにリダイレクト
    else:
        form = ContributionForm()
    return render(request, 'point/create.html', {'form': form})

def point_success(request):
    return render(request, 'point/point_success.html')