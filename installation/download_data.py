import sys, os, zipfile, tarfile
import urllib.request
import requests

#where_to_save = '../Data/'
where_to_save = 'Data/'

#create data directory
if not os.path.exists(where_to_save):
    os.makedirs(where_to_save)
    
#import Klee painting
url = 'https://img.myswitzerland.com/671846/407'  
urllib.request.urlretrieve(url, where_to_save+'Klee.jpg')