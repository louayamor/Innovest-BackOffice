from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.db.models import Sum
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import User as u, Business, Investment, UserProfile
from django import forms
from django.shortcuts import redirect
from django.views.generic import FormView
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.db.models import Q


def dashboard(request):
    context = {
        'title': 'Dashboard',  
    }
    return render(request, 'dashboard.html', context)

def users(request):
    active_users = u.objects.filter(is_active=True)
    investor_users = u.objects.filter(is_investor=True)
    users = u.objects.all() 
    users_count = users.count() 

    query = request.GET.get('search_query')
    if query:
        users = users.filter(Q(username__icontains=query) | Q(email__icontains=query))

    return render(request, 'users.html', {'users': users,
                                           'users_count': users_count, 
                                           'active_users': active_users, 
                                           'investor_users': investor_users,
                                           'query': query,
                                           })

def businesses(request):
    business_aggregates = Business.objects.aggregate(
    total_revenue=Sum('revenue'),
    total_profit=Sum('profit')
    )
    total_revenue = business_aggregates.get('total_revenue', 0)
    total_profit = business_aggregates.get('total_profit', 0)
    businesses = Business.objects.all()  
    businesses_count = businesses.count()
    return render(request, 'businesses.html', {'businesses': businesses,
                                                'businesses_count': businesses_count,
                                                'total_revenue': total_revenue,
                                                'total_profit': total_profit,
                                                })

def investments(request):
    investments = Investment.objects.all()
    investments_count = investments.count()
    total_amount_invested = investments.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    return render(request, 'investments.html', {'investments': investments, 
                                                'investments_count': investments_count,
                                                  'total_amount_invested': total_amount_invested
                                                  })

def sectors(request):
    sectors = [
        'Information Technology',
        'Finance and Banking',
        'Healthcare Services',
        'Retail and E-commerce',
        'Real Estate',
        'Manufacturing',
        'Education and Training',
        'Hospitality and Tourism',
        'Transportation and Logistics',
        'Media and Entertainment',
        'Energy and Utilities',
    ]

    sector_counts = []
    for sector in sectors:
        count = Business.objects.filter(sector=sector).count()
        sector_counts.append({'sector': sector, 'count': count})

    context = {
        'sector_counts': sector_counts,
    }
    return render(request, 'sectors.html', context)

class LoginViaUsernameForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'))

    @property
    def field_order(self):
        return ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        user = u.objects.filter(username=username).first()
        
        if not user:
            raise ValidationError(_('Invalid username or password'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user
        return username


class LoginView(FormView):
    template_name = 'authentication-login.html'
    form_class = LoginViaUsernameForm
    success_url = reverse_lazy('dashboard')  # Assuming 'dashboard' is the name of your dashboard URL pattern

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, _('Invalid username or password'))
            return self.form_invalid(form)

def count_users(request):
    users_count = u.objects.count()
    return render(request, 'count_users.html', {'users_count': users_count})

def count_businesses(request):
    businesses_count = Business.objects.count()
    return render(request, 'count_businesses.html', {'businesses_count': businesses_count})

def count_investments(request):
    investments_count = Investment.objects.count()
    return render(request, 'count_investments.html', {'investments_count': investments_count})

def delete_user(request, user_id):
    user = get_object_or_404(u, id=user_id)
    if request.method == 'POST':
        Business.objects.filter(owner=user).delete()
        UserProfile.objects.filter(user=user).delete()
        user.delete()
        return redirect('users')
    return render(request, 'users.html')

from django.utils import timezone

def add_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not u.objects.filter(username=username).exists() and not u.objects.filter(email=email).exists():
            current_datetime = timezone.now()
            user = u(username=username, email=email, is_active=True, is_verified=True,created_at=current_datetime, is_investor= False)
            user.password = make_password(password)  
            user.roles = ["ROLE_ADMIN"] 

            user.save()
            return HttpResponse('Admin user created successfully!')
        else:
            return HttpResponse('Username or email already exists!')

    return render(request, 'add_admin.html')

def searchUser(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            users = u.objects.filter(username__icontains=query)
        else:
            users = u.objects.all()
        return render(request, 'search_users.html', {'users': users, 'query': query})
    else:
        return render(request, 'search_users.html')