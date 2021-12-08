from django.views.generic import ListView

from catalogapp.models import ProductItem, ProductCategory


class IndexPageView(ListView):
    model = ProductItem
    template_name = 'catalogapp/goods_list.html'
    paginate_by = 10

    def get_queryset(self):
        return ProductItem.objects.prefetch_related('product_category').all()

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['all_cats'] = ProductCategory.objects.all()
        return context


class CategoryPageView(ListView):
    model = ProductItem
    template_name = 'catalogapp/category_list.html'
    paginate_by = 10

    def get_queryset(self):
        return ProductItem.objects.filter(
            product_category=self.kwargs['pk']).prefetch_related(
            'product_category').order_by(
            'product_category__productitem__added')

    def get_context_data(self, **kwargs):
        context = super(CategoryPageView, self).get_context_data(**kwargs)
        context['all_cats'] = ProductCategory.objects.all()
        context['category_name'] = ProductCategory.objects.filter(
            pk=self.kwargs['pk']).first()
        return context
