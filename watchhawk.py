#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import time
from datetime import datetime
import re
from fsmonitor import FSMonitor, FSMonitorThread
from jinja2 import Environment, FileSystemLoader

TEMPLATE_FOLDERS = ('templates', 'templates/pages')
MAIN_TEMPLATE = 'index.html'
DESTINATION = 'index.html'
INTERVAL = .2

def change_detected(watching=True):
    if watching: print('%s: Change detected... ' % datetime.now().strftime("%H:%M:%S") , end='')
    try:
        # recompile jinja template
        env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDERS), extensions=['jinja2.ext.with_', 'jinja2.ext.autoescape'])
        template = env.get_template(MAIN_TEMPLATE)
        result = template.render()
        # save the results
        with open(DESTINATION, 'wb') as f:
            f.write(result.encode('UTF-8'))
    except Exception, e:
        if watching: print('failed!')
        else: raise e
    else:
        if watching: print('written!')

def watch():
    print(">>> I'm watching the '%s' folder%s like a HAWK!" % ("', '".join(TEMPLATE_FOLDERS), "s" if len(TEMPLATE_FOLDERS) > 1 else ""))
    print(">>> I lost my glasses! Thus, folders might not be watched recursively!")
    m = FSMonitorThread(callback=lambda event: change_detected())
    for dir in TEMPLATE_FOLDERS:
        m.add_dir_watch(dir)
    # FSMonitorThread is a daemon thread and we can't change that :(
    # ... so we use this opportunity to clean up
    try:
        while True:
            if raw_input():
                change_detected(watching=True)
    except KeyboardInterrupt:
        m.stop()
        del m
        print("\n>>> Watch you next time...")
        exit(0)


def compile():
    change_detected(watching=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the operation type. One of: 'watch', 'compile'")
    elif sys.argv[1] == 'watch':
        watch()
    elif sys.argv[1] == 'compile':
        compile()
    else:
        print("The given operation type was not recognized. Use one of: 'watch', 'compile'")



    

