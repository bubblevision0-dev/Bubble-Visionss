
from django.utils.cache import add_never_cache_headers

class DisableClientSideCachingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # We only apply this to logged-in users to prevent 
        # private dashboards from being cached in the browser.
        if request.user.is_authenticated:
            add_never_cache_headers(response)
        return response
