from celery import Celery
import sys
import os
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
        return x + y
    
def airfoil(angle, n_levels, n_nodes):
        resultFile = '../murtazo/navier_stokes_solver/results/drag_ligt.m'
        subprocess.call('sh runAirfoil.sh {0} {1} {2}'
                        .format(angle, n_levels, n_nodes))
        with open(resultFile, 'r'):
                return results.read()
        
