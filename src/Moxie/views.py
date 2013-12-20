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
    

def job(request):
    return HttpResponse(jobs.next())

def reset(request):
    jobs.reset()
    return HttpResponse("MockHost - reset\n")