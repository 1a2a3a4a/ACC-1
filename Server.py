#!flask/bin/python
from flask import Flask, jsonify
import sys
# import Celery
import subprocess
from create_instance import create_worker
from worker import airfoil
app = Flask(__name__)


@app.route('/post/<int:angle_start>/<int:angle_stop>/<int:n_angles>/<int:n_nodes>/<int:n_levels>')
# postURL:
#   http://127.0.0.1:5000/post/angle_start/angle_stop/n_angles/n_nodes/n_levels
# example:
#   http://127.0.0.1:5000/post/0/30/10/200/3
def run_app(angle_start, angle_stop, n_angles, n_nodes, n_levels):
    # Do something with the arguments
    # angles = generate_angles(angle_start, angle_stop, n_angles)
    # tasks = push_tasks(angles, n_levels, n_nodes)
    # Todo: Get results from tasks and return something

    #Run source script    
    subprocess.call('sh source.sh', shell=True)
    #Start worker
    create_worker()
    #Add task
    result = airfoil.delay(angle_start,
                           angle_stop,
                           n_angles,
                           n_nodes,
                           n_levels).get()
    
    # return result

def generate_angles(angle_start, angle_stop, n_angles):
    angles = []
    angle_diff = (angle_stop - angle_start) / n_angles;
    for i in range(n_angles + 1):
        angle = angle_start + angle_diff*i
        angles.append(angle)
    return angles

def push_tasks(angles, n_levels, n_nodes):
    tasks = []
    for a in angles:
        for r in range(n_levels+1):
            print 'Pushing task: r%da%dn%d' % (r, a, n_nodes)
            #Todo: Implement task
            #      Add task to queue and append return value to tasks
            #tasks.append(task(a,r,n_nodes).delay())
    return tasks

if __name__ == '__main__':    
    app.run(host='0.0.0.0',debug=True)
