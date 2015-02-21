Create a S3 pre-Signed URL
======================================
Prerequisites
--------------

1.  Make sure you have installed **Python** https://www.python.org/downloads/

2.  Install **Pip** from https://pip.pypa.io/en/latest/. Pip is required to to install boto. 
    Start by downloading pip from https://bootstrap.pypa.io/get-pip.py and then install it using the command ``python get-pip.py``. To upgrade pip on Linux run command ``pip install -U pip``

3.  AWS SDK for Python is called **Boto**. You can find more information here http://aws.amazon.com/sdk-for-python
    To install Boto run command ``pip install boto``. Alternatively you can install Boto from git by running :
    
    | ``git clone git://github.com/boto/boto.git``  
    | ``cd boto``  
    | ``python setup.py install``  
    
4.  Configure **Boto credentials**: Information about Boto configuration is available here - https://boto.readthedocs.org/en/latest/boto_config_tut.html. Depending on the OS you use, the configuration may vary. In Linux and MAC a file named ``/etc/boto.cfg`` for all users or ``~/.boto`` for single user has to be created. The content of the file should have the following lines. If you are using IAM roles with S3 access on an EC2 instances, this step can be ignored.
    
  | ``[Credentials]``  
  | ``aws_access_key_id = <your_access_key_here>``  
  | ``aws_secret_access_key = <your_secret_key_here>``  


S3 pre-signed URLs
-------------------

1.	More information about S3 pre-signed URLs can be found here --> http://docs.aws.amazon.com/AmazonS3/latest/dev/ShareObjectPreSignedURL.html

2.	To create a pre-signed URL using this script, enter the **S3 bucketname** containing the object, **the path of the object** in the bucket and the **duration** for the object to be accessible.

3.  To execute the downloaded code use the following command ``python s3-signed-url.py``
