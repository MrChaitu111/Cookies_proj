from django.shortcuts import render, redirect
from django.core.cache import cache

# --- Cookies Page ---
def home(request):
    username = request.COOKIES.get('username')
    if request.method == 'POST':
        username = request.POST.get('username')
        response = render(request, 'home.html', {'cookie_value': username, 'cookie_age': 5})
        response.set_cookie('username', username, max_age=5)
        return response
    return render(request, 'home.html', {'cookie_value': username, 'cookie_age': 5})


# --- Sessions Page ---
def session_page(request):
    username = request.COOKIES.get('username')
    if not username:
        return redirect('home')

    request.session['username'] = username
    request.session.set_expiry(5)
    session_user = request.session.get('username')
    return render(request, 'session.html', {'session_user': session_user})


# --- Cache Page ---
def cache_page(request):
    username = request.session.get('username')
    if not username:
        return redirect('session_page')

    cache.set('username_cache', username, timeout=5)
    cached_user = cache.get('username_cache')
    return render(request, 'cache.html', {'cached_user': cached_user})
