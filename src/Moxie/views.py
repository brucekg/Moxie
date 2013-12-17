'''
Created on Dec 17, 2013

@author: brucekg
'''

from django.http import HttpResponse

from mock_jobs import MockJobs

jobs = MockJobs('/opt/ot/jobs')

def home(request):
    return HttpResponse("MockHost")

def job(request):
    return HttpResponse(jobs.next())

def stopped(request):
    jobs.reset()
    return HttpResponse("Stopped - reset jobs")
