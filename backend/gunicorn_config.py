from multiprocessing import cpu_count

bind = '0.0.0.0:8000'
worker_class = 'gevent'
workers = 2 * cpu_count() + 1
accesslog = '-'
errorlog = '-'