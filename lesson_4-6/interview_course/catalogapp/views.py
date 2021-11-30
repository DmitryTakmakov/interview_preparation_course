from django.views.generic import ListView

from catalogapp.models import ProductItem


class IndexPageView(ListView):
    model = ProductItem
    template_name = 'catalogapp/goods_list.html'

    def get_queryset(self):
        return ProductItem.objects.all()
