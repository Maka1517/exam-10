from django.contrib.auth import get_user_model
from django.shortcuts import render

from webapp.views.base_view import SearchView
from accounts.models import Profile


class IndexView(SearchView):
    template_name = 'index.html'
    context_object_name = 'profiles'
    paginate_by = 2
    paginate_orphans = 0
    model = get_user_model()
    # ordering = ['-created_at']
    search_fields = ['first_name__icontains', 'last_name__icontains']

