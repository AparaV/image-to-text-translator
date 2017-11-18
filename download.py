##########################
##
## Download MNIST dataset
##
##########################

import os
import gzip
import shutil
import requests

DIR = "data"
BASE_URL = "http://yann.lecun.com/exdb/mnist/"
FILES = ["t10k-images", "t10k-labels", "train-images", "train-labels"]
FORMAT_IMAGE = "idx3-ubyte"
FORMAT_LABEL = "idx1-ubyte"

def download_extract(url, fname):
	'''
		Download from url and extract into fname
	'''
	
	response = requests.get(url)
	with open('temp.gz', 'wb') as f:
		f.write(response.content)

	with gzip.open('temp.gz', 'rb') as f_in, open(fname, 'wb') as f_out:
		shutil.copyfileobj(f_in, f_out)
	
	os.remove("temp.gz")
	
if __name__ == "__main__":

	if not os.path.exists(DIR):
		os.makedirs(DIR)
	
	for file in FILES:
		if "label" in file:
			url = BASE_URL + file + "-" + FORMAT_LABEL + ".gz"
			fname = os.path.join(DIR, file + "." + FORMAT_LABEL)
		else:
			url = BASE_URL + file + "-" + FORMAT_IMAGE + ".gz"
			fname = os.path.join(DIR, file + "." + FORMAT_IMAGE)
		print("Downloading {}".format(file))
		download_extract(url, fname)