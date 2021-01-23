from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
# from django.shortcuts import render
from django.views.generic.base import View
# from rest_framework.authtoken.admin import User
from rest_framework.generics import get_object_or_404

from webapp.views.base_view import SearchView
from accounts.models import Profile, FriendList


class IndexView(SearchView):
    template_name = 'index.html'
    context_object_name = 'profiles'
    paginate_by = 2
    paginate_orphans = 0
    model = get_user_model()
    # ordering = ['-created_at']
    search_fields = ['first_name__icontains', 'last_name__icontains']


class FriendChoseView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        chosen_friend = get_object_or_404(Profile, pk=kwargs.get('pk'))
        like, created = FriendList.objects.get_or_create(profile=chosen_friend, user=request.user)
        if created:
            chosen_friend.save()
            return HttpResponse()
        else:
            return HttpResponseForbidden()


class FriendDelView(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        friend = get_object_or_404(Profile, pk=kwargs.get('pk'))
        like = get_object_or_404(friend.friends, user=request.user)
        like.delete()
        friend.save()
        return HttpResponse()