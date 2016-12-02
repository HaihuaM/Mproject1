
class RSH_RUNNER:
	__runner_requestor__        =    ''
	__operating_machine__       =    ''
	__log_path__                =    ''
	__parellel_exec__           =    false
	__parellel_proc__           =    0
	__command_queue__           =    []
	__log_id__                  =    ''
	

	self.__init__(self,requestor,machine,log_path,parellel_proc,command_queue):
		self.__runner_requestor__        =    requestor
		self.__operating_machine__       =    machine
		self.__log_path__                =    log_path
		self.__parellel_proc__           =    parellel_proc
		sefl.__command_queue__           =    command_queue

	def __run__(self):
		"""
		func run is the wrapper for the real run
		"""
		from logging import getLogger, INFO
		from cloghandler import ConcurrentRotatingFileHandler
		import multiprocessing,subprocess
		import os,time
		
		log = getLogger()
		# buid log path
		sefl.__log_id__    = self.__runner_requestor__+'_'+time.time()+'.log'
		logfile = os.path.join(log_path,self.__log_id__)

		# Rotate log after reaching 10M, keep 5 old copies.
		rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 1024*1024*10, 5)
		log.addHandler(rotateHandler)




		log.setLevel(INFO)
		log.setLevel(error)
		
		log.info("Here is a very exciting log message, just for you")


