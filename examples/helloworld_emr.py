### First attempt to run a "hello world" file on several instances(?) on AWS

import time
from datetime import datetime
from boto.emr.step import StreamingStep
from boto.emr.connection import EmrConnection

job_ts = datetime.now().strftime("%Y%m%d%H%M%S")
emr = EmrConnection()

# Python files must be hosted on s3 and linked to for execution.
## [ ] TODO(emmagras): Check the docs for StreamingStep and understand
##     the arguments below.
wc_step = StreamingStep('wc text', \
  's3://elasticmapreduce/samples/wordcount/wordSplitter.py', \
  'aggregate', input='s3://elasticmapreduce/samples/wordcount/input', \
  output='s3://wc-test-bucket/output/%s' % job_ts)
jf_id = emr.run_jobflow('wc jobflow', 's3n://emr-debug/%s' % job_ts, \
  steps=[wc_step])

while True:
  jf = emr.describe_jobflow(jf_id)
  print "[%s] %s" % (datetime.now().strftime("%Y-%m-%d %T"), jf.state)
  if jf.state == 'COMPLETED':
    break
time.sleep(10)
