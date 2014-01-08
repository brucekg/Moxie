'''
Created on Dec 17, 2013

@author: brucekg
'''

import os.path
import json

class MockJobs(object):

    def __init__(self):
        self.jobs = []
        self.index = 0
        self.data = None
        return
        
    def load(self, source):
        f = open(source,'r')
        buf = f.read()
        f.close()
        
        jobs = []
        jobs.append(json.loads(buf))
        
        self.jobs = jobs
        self.reset()
        
        fn = os.path.dirname(source)+'/MockJobs.json'
        if os.path.exists(fn):
            if os.path.isfile(fn):
                data = open(fn, 'r').read()
                self.data = json.loads(data)
                self.data['job_id'] = int(self.data['job_id'])
            else:
                raise Exception("%s is not a file." % fn)
        else:
            self.data = {"job_id":1000}
        
        self.fn = fn

        return
    
    def reset(self):
        
        self.index = 0
        return
    
    def next(self):
        
        if self.data == None:
            return "MockJobs - Jobs Not Loaded\n"
        
        if self.index < len(self.jobs):
            d = self.jobs[self.index]
            if d['job_id'] == '0':
                d['job_id'] = str(self.data['job_id'])
                self.data['job_id'] += 1
            r = json.dumps(d)
            open(self.fn, 'w').write(json.dumps(self.data))
            self.index += 1
        else:
            r = '{"operation":"stop"}'
        return r
