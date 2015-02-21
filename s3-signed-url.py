import boto
import time

bucketname = raw_input("Enter the name of the bucket. Eg: mybucket: ")
objectpath = raw_input("Enter the path of the object you would like to access. Eg: /directoryname/testfile.txt : ")
timevalid = int(input("Enter the time of validity for the object in seconds. Eg: 1500: "))


s3conn = boto.connect_s3() # 's3conn' is a variable that is connecting to boto.
bucketconn = s3conn.get_bucket(bucketname) # connecting to the bucket entered.


object_key = bucketconn.get_key(objectpath)
object_url = object_key.generate_url(timevalid, query_auth=True) # you could use the following if you do not want to use https - object_url = object_key.generate_url(timevalid, query_auth=True, force_http=True)
print " "
print "The Pre-Signed URL for s3://" + bucketname + objectpath + " is : "
print "----------------------------------------------------------------"
print object_url
print "----------------------------------------------------------------"
