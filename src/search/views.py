
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, Categoria, SubCategoria
from fast_autocomplete import AutoComplete
# Create your views here.

class SearchProductView(ListView):                #class based view

        template_name = "search/view.html"

        def get_context_data(self, *args, **kwargs):
            words = SubCategoria.objects.all
            # autocomplete = AutoComplete(words=words)
            context = super(SearchProductView, self).get_context_data(*args, **kwargs)
            context['query'] = self.request.GET.get('q')
            query = self.request.GET.get('q')
            context['query'] = query
            # return autocomplete.search(context)
            # SearchQuery.objects.create(query=query)
            return context

        def get_queryset(self, *args, **kwargs):
            words = SubCategoria.objects.all
            request = self.request
            method_dict = request.GET
            query = method_dict.get('q', None)        # method_dict['q']
            # autocomplete = AutoComplete(words=words)
            if query is not None:
                # return autocomplete.search(query)
                return Product.objects.search(query)
            return Product.objects.featured()
            '''
            __icontains = field contains this
            __iexact = field is exactly this

            '''
