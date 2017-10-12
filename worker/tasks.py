from celery import Celery
import sys
import os
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
        return x + y
    
def airfoil(start_angle, stop_angle, n_angles, n_levels, n_nodes):
        result = ""
        resultFile = '../murtazo/navier_stokes_solver/results/drag_ligt.m'
        subprocess.call('sh runAirfoil.sh {0} {1} {2} {3} {4} {5}'.format(start_angle, stop_angle, n_angles, n_nodes, n_levels))
        with open(resultFile, 'r') as f:
                result = f.read()
        subprocess.call('sh cleanWorker.sh')
        return result
