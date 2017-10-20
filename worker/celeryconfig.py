import os
broker_url = 'pyamqp://myuser:mypassword@' + os.environ.get('BROKER_IP') + ':5672/myvhost'
result_backend = 'rpc://'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Stockholm'
enable_utc = True
