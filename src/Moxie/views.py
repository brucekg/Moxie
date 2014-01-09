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
    
def param(request):
    value = request.GET['none']
    if value != None:
        jobs.none_limit = int(value)
    return HttpResponse("MockHost - param\n")
    
def job(request):
    return HttpResponse(jobs.next())

def reset(request):
    jobs.reset()
    return HttpResponse("MockHost - reset\n")

def record(request):
    #TODO: display POST
    return HttpResponse("MockHost - record == %s\n" % request.body)
