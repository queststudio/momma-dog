from multiprocessing import cpu_count

bind = '0.0.0.0:8088'
worker_class = 'gevent'
workers = 1 #2 * cpu_count() + 1
accesslog = '-'
errorlog = '-'