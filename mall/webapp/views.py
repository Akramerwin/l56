from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import MultipleObjectMixin
from webapp.models import Stufs, Stufs_in_cart
from webapp.forms import StufsForm, SimpleSearchForm, StufsCartForm
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, DetailView, CreateView, DeleteView, UpdateView, View
from django.db.models import Q




class index_views(ListView):
    template_name = 'index.html'
    context_object_name = 'stufs'
    model = Stufs
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        if self.form.is_valid():
            self.search_value = self.form.cleaned_data['search']
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(stuf__icontains=self.search_value)
            queryset = queryset.filter(query)
            return queryset
        if not self.search_value:
            filter = Stufs.objects.exclude(remainder=0).order_by('stuf')
            return filter


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class stufs_view(DetailView):
    template_name = 'stufs_view.html'
    model = Stufs


class stuf_create(CreateView):
      template_name = 'stufs_create.html'
      model = Stufs
      form_class = StufsForm

class stuf_update_view(UpdateView):
      template_name = 'update.html'
      form_class = StufsForm
      model = Stufs
      context_object_name = 'stuf'


class stuf_delete_view(DeleteView):
      template_name = 'delete.html'
      model = Stufs
      context_object_name = 'stuf'
      success_url = reverse_lazy('index')

class stuf_in_the_bag(View):
      template_name = 'indexback.html'
      model = Stufs_in_cart

      def get(request, *args, **kwargs):
          stuf = get_object_or_404(Stufs, pk=kwargs.get('pk'))
          if Stufs_in_cart.objects.filter(stuf_key_id=stuf.pk):
              stufs_in_cart = Stufs_in_cart.objects.get(stuf_key=stuf)
              if stuf.remainder> 0:
                  stufs_in_cart.amount_stuf += 1
                  stufs_in_cart.save()
                  stuf.remainder -= 1
                  stuf.save()
                  return redirect("index")
              elif stuf.remainder == 0:
                  pass
          else:
              cart = Stufs_in_cart.objects.create(stuf_key=stuf)
              cart.amount_stuf = 1
              cart.save()
              stuf.remainder -= 1
              stuf.save()
              return redirect("index")

class stuf_bag_list(ListView):
    template_name = 'indexback.html'
    model = Stufs_in_cart
    context_object_name = 'bag'

class delete_stuf(DeleteView):
    template_name = 'delete_stuf.html'
    model = Stufs_in_cart
    context_object_name = 'stuf'
    success_url = reverse_lazy('stuflist')