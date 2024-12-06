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

#追加
from .models import Item
class ItemListView(TemplateView):
    template_name = 'test/item_list.html'  # 使用するテンプレートを指定

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_type = self.request.GET.get('type', 'all')  # カテゴリフィルタ
        order = self.request.GET.get('order', 'asc')    # 並べ替え（デフォルトは昇順）

        # アイテムの取得とフィルタリング
        items = Item.objects.all()
        if item_type != 'all':
            items = items.filter(type=item_type)

        # 並べ替え
        if order == 'asc':
            items = items.order_by('point')  # 昇順
        elif order == 'desc':
            items = items.order_by('-point')  # 降順

        # コンテキストにデータを渡す
        context['items'] = items
        context['selected_type'] = item_type
        context['selected_order'] = order
        return context
 
class ItemDetailView(TemplateView):
    template_name = 'test/item_detail.html'  # 詳細ページのテンプレート

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # URLのパラメータから商品ID (pk)を取得し、詳細情報を取得
        pk = self.kwargs['pk']
        item = Item.objects.get(pk=pk)
        context['item'] = item
        return context

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