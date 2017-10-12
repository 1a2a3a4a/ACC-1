from celery import Celery
import sys
import os
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
        return x + y
    
def airfoil(angle, n_levels, n_nodes):
        solver_path = '../murtazo/navier_stokes_solver/'
        #subprocess.call('.{0}/airfoil {1} {1} {2} {3}'
        #                .format(solver_path, angle, n_levels, n_nodes))
        with open(solver_path+'results/drag_ligt.m', results):                
                return results.read()
        
