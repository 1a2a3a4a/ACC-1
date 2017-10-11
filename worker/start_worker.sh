cd /home/fenics/shared/ACC-1/worker/;
git pull;
celery -A tasks worker;
