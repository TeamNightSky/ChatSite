from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r"cdn", "cdn.urls", name="cdn")
)
