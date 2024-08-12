from django.core.cache import cache
from django.shortcuts import render

def rate_limited(view_func):
    def _wrapped_view(request, *args, **kwargs):
        ip = get_client_ip(request)
        rate_limit_key = f'rate_limit_{ip}'
        request_count = cache.get(rate_limit_key, 0)
        if request_count >= 10:
            return render(request, 'error.html', {'errorCode': 429, 'error': 'Too Many Requests'})
        cache.set(rate_limit_key, request_count + 1, timeout=86400) 
        return view_func(request, *args, **kwargs)
    
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    return _wrapped_view
