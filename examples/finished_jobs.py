import redis
from rq import Connection
from rq.job import FinishedJobs, Job

conn = redis.from_url('redis://localhost:6379')

if __name__ == '__main__':
    with Connection(conn):
    	fj = FinishedJobs()
    	res = fj.poll()
    	if res:
    		print res.to_dict()
    	else:
    		print "Empty FinishedJobs"