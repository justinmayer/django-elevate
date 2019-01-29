from django.utils import http

def is_safe_url(url, allowed_hosts, require_https):
    # This is the compat function for older Django versions
    return http.is_safe_url(url=url, host=allowed_hosts)
