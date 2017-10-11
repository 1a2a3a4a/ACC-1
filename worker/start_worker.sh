cd /home/fenics/local/ACC-1/worker/;
git pull;
celery -A tasks worker;
