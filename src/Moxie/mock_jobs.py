'''
Created on Dec 17, 2013

@author: brucekg
'''

import json

class MockJobs(object):

    def __init__(self):
        self.jobs = []
        self.index = 0
        self.data = None
        self.none_limit = 0
        self.none_count = 0
        return
        
    def load(self, source):
        f = open(source,'r')
        buf = f.read()
        f.close()
        
        jobs = []
        jobs.append(json.loads(buf))
        
        self.jobs = jobs
        self.reset()
        
        return
    
    def reset(self):
        
        self.index = 0
        return
    
    def next(self):
        
        if self.index < len(self.jobs):
            d = self.jobs[self.index]
            r = json.dumps(d)
            self.index += 1
            self.none_count = 0
        else:
            if self.none_count >= self.none_limit:
                r = '{"operation":"stop"}'
            else:
                r = '{"operation":"none"}'
                self.none_count += 1
                
        return r
