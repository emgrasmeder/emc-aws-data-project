### The purpose of this file is primarily to translate the Python language
### into human-readable function names for the PM, who is inexperienced with 
### OOP, but will need to use Python to compute on AWS

import boto
import boto.s3.connection
import credentials
import traceback


file_name = "test.csv"

def get_function_name():
    return str(traceback.extract_stack(None, 2)[0][-2]+"...")
    
def get_current_file_directory():
    print get_function_name()
    import os, sys  #, inspect \n full_file_path = print inspect.stack()[0][1]   
    current_file_directory = \
        os.path.abspath(os.path.split(sys.argv[0])[0])
    return current_file_directory
    return current_file_directory
    
def connect_to_s3():
    print get_function_name()
    new_connection = boto.connect_s3(
        aws_access_key_id = credentials.key(),
        aws_secret_access_key = credentials.secret(),
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
    return new_connection
    
def list_all_buckets():
    print get_function_name()
    get_function_name()
    for bucket in new_connection.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
        
def create_new_bucket(bucket_name):
    print get_function_name()
    return new_connection.create_bucket(bucket_name)
    
    
def list_bucket_content(bucket_obj):
    print get_function_name()
    for key in bucket_obj.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )
                
def retrieve_bucket_object(bucket_name):
    print get_function_name()
    return new_connection.get_bucket(bucket_name)
                
def upload_from_path(bucket_obj,current_file_directory, file_name):
    from boto.s3.key import Key
    print get_function_name()
    key_instance = Key(bucket_obj)
    key_instance.key = ("hopefully_name_of_key_instance")
    key_instance.set_contents_from_filename(file_name)
    # key_instance.set_contents_from_filename(current_file_directory +\
        # "\\" + "very_fake_data.csv")
    key_instance.get_contents_to_filename("mcptest_output.csv")
    #"C:\Users\wag\Desktop\mcptest_output.csv"
    return key_instance
 
def download_file_to_computer(key_instance, file_name, download_to_path):
    print get_function_name()
    key_instance.get_contents_to_filename(file_name+"_downloaded_from_s3" )
    

current_file_directory = get_current_file_directory()
new_connection = connect_to_s3()    

# bucket = create_new_bucket("name_of_example_bucket") #uncomment to execute

bucket_obj = retrieve_bucket_object("name_of_example_bucket")

key_instance = upload_from_path(bucket_obj, \
        current_file_directory, file_name)
list_bucket_content(bucket_obj) # not working, not needed.

download_to_path = current_file_directory
download_file_to_computer(key_instance, file_name, download_to_path)
