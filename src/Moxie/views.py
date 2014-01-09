'''
Created on Dec 17, 2013

@author: brucekg
'''

from django.http import HttpResponse

from mock_jobs import MockJobs

jobs = MockJobs()

def load(request):
    source = request.GET['source']
    jobs.load(source)
    return HttpResponse("MockHost - load\n")

def local(request):
    source = request.GET['source']
    job_source = open(source,'r').read()
    return HttpResponse(job_source)
    
def job(request):
    return HttpResponse(jobs.next())

def reset(request):
    jobs.reset()
    return HttpResponse("MockHost - reset\n")

def record(request):
    return HttpResponse("MockHost - record\n")
