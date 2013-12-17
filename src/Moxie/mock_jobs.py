'''
Created on Dec 17, 2013

@author: brucekg
'''

class MockJobs(object):

    def __init__(self, source):
        
        f = open(source,'r')
        buf = f.read()
        f.close()
        
        jobs = []
        i = 0
        while i < len(buf):
            j = buf.find('{', i)
            if j == -1:
                break
            k = buf.find('}', j)
            if k == -1:
                break
            k += 1
            
            jobs.append(buf[j:k])
            i = k
        
        self.jobs = jobs
        self.reset()
        return
    
    def reset(self):
        
        self.index = 0
        return
    
    def next(self):
        
        if self.index < len(self.jobs):
            r = self.jobs[self.index]
            self.index += 1
        else:
            r = '{"operation":"stop"}'
        return r
