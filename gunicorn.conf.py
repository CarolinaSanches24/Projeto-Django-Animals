import os

bind = "[::]:8000"
workers = 3
worker_class = 'sync'
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 1000