#!flask/bin/python
from flask import Flask, jsonify
import sys
import time
import celery
import subprocess
from create_instance import create_worker
import tasks
app = Flask(__name__)

#Stick to maximum of 4 workers to not flood the cloud with instances
max_workers = 4

number_of_workers = 0



@app.route('/post/<int:angle_start>/<int:angle_stop>/<int:n_angles>/<int:n_nodes>/<int:n_levels>')
# postURL:
#   http://127.0.0.1:5000/post/angle_start/angle_stop/n_angles/n_nodes/n_levels
# example:
#   http://127.0.0.1:5000/post/0/30/10/200/3
def run_app(angle_start, angle_stop, n_angles, n_nodes, n_levels):
    start_time = time.time()
    #Run source script    
    #subprocess.call('sh source.sh', shell=True)

    #Generate angles
    angles = generate_angles(angle_start, angle_stop, n_angles)
    taskList = create_tasks(angles, n_levels, n_nodes)
    #Create workers
    for _ in range(min(taskList, max_workers) - number_of_workers):
        create_worker()
        
    taskList = map(lambda task: (task[0], tasks.airfoil.delay(task[1][0], task[1][1], task[1][2], task[1][3], task[1][4])), taskList)

    #Wait for tasks to be processed and then return results
    while True:
        if all(t[1].ready() == True for t in taskList):
            result = map(lambda task: (task[0], task[1].result), taskList)
            print("--- %s seconds ---" % (time.time() - start_time))
            return result_to_flask(result)
        else:
            time.sleep(0.1)
        
def result_to_flask(result):
    result_joined = map(lambda result_tuple: "<p>" + result_tuple[0] + ":" + result_tuple[1].replace('\n', '<br>') + "</p>", result)
    return "".join(result_joined)

def generate_angles(angle_start, angle_stop, n_angles):
    angles = []
    angle_diff = (angle_stop - angle_start) / n_angles;
    for i in range(n_angles):
        angle = angle_start + angle_diff*i
        angles.append(angle)
    return angles

def create_tasks(angles, n_levels, n_nodes):
    tasks = []
    for a in angles:
        for r in range(n_levels+1):
            print 'Creating task: r%da%dn%d' % (r, a, n_nodes)
            taskName = 'r%da%dn%d' % (r, a, n_nodes)
            # Add task to queue and append return value to tasks
            tasks.append((taskName, (a,a,1,n_nodes,r)))
    return list(set(tasks))

if __name__ == '__main__':    
    app.run(host='0.0.0.0',debug=True)
