import io
from google.cloud import vision
from google.cloud.vision import types


def get_image_labels():

	try:
		vision_client = vision.ImageAnnotatorClient('account_key.json')
	except:
		print("Error connecting to google api: check account key")

	x = 1000
	z=".jpg"
	working = 0
	while True:
		try:
			file_name_base = "twitterimage"
			y = str(x)
			x = x+1
			file_name = file_name_base + y + z
			with io.open(file_name, 'rb') as image_file:
				working = 1
				content = image_file.read()
				image = vision.types.Image(content=content)

			response = vision_client.label_detection(image=image)
			labels = response.label_annotations
			working = 2
			r = x-1000
			print("description of photo ",r,": ")
			for label in labels:
				print(label.description)

		except:
			if(working==0):
				print("No image files found")
			if(working==1)
				print("Error getting label from photo: check internet connection")
			break


if __name__=='__main__':

	get_image_labels()
