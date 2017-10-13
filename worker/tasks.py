from celery import Celery
import subprocess
import sys
import os
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task    
def airfoil(start_angle, stop_angle, n_angles, n_nodes, n_levels):
        result = ""
        resultFile = '../murtazo/navier_stokes_solver/results/drag_ligt.m'
        subprocess.call('sh -x runAirfoil.sh {0} {1} {2} {3} {4}'.format(start_angle, stop_angle, n_angles, n_nodes, n_levels), shell=True)
        with open(resultFile, 'r') as f:
                result = f.read()
        subprocess.call('sh -x cleanWorker.sh', shell=True)
        return result
