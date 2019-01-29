from django.http.utils import is_safe_url

def is_safe_url(url, allowed_hosts):
    # This is the compat function for older Django versions
    return is_safe_url(url, host=allowed_hosts)
