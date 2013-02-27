from __future__ import print_function
import sys
import time
import re
from fsmonitor import FSMonitor
from jinja2 import Environment, FileSystemLoader

TEMPLATE_FOLDER = 'templates'
MAIN_TEMPLATE = 'index.html'
DESTINATION = 'index.html'
INTERVAL = .2

def change_detected(talky=True):
    if talky: print('Change detected... ', end='')
    # recompile jinja template
    env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))
    template = env.get_template(MAIN_TEMPLATE)
    result = template.render()
    # save the results
    with open(DESTINATION, 'wb') as f:
        f.write(result)
    if talky: print('written!')

def watch():
    m = FSMonitor()
    m.add_dir_watch(TEMPLATE_FOLDER)
    while True:
        for evt in m.read_events():
            time.sleep(INTERVAL)
            change_detected()

def compile():
    change_detected(talky=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the operation type. One of: 'watch', 'compile'")
    elif sys.argv[1] == 'watch':
        watch()
    elif sys.argv[1] == 'compile':
        compile()
    else:
        print("The given operation type was not recognized. Use one of: 'watch', 'compile'")



    

