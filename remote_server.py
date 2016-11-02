#!/usr/bin/python
import os,sys,re


def job_monitor(path):
	job_list=[]
	if os.path.exists(path):
		for x in [ job for job in os.listdir(path) if job.split('_')[0] == 'JID' ] :
			job_list.append(x)
		return job_list
	else:
		print 'path not exist'
		return []


def job_exec(job,workpath):
	ret=os.popen("sh -f %s" %(os.path.join(workpath,job))).read()
	#print "sh -f %s" %(os.path.join(workpath,job))
	print ret
	f=open(os.path.join(workpath,"log.%s" %job),'w')
	f.write(ret)
	f.close()
	os.system("touch  %s/'.%s_done' " %(work_path,job))



work_path='/home/Esblick/git_workplace/Mproject1/testdir'
for job in job_monitor(work_path):
	job_exec(job,work_path)
