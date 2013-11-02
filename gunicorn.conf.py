import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'error'
max_requests = 1000
