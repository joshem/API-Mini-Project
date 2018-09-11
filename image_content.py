import io
from google.cloud import vision
from google.cloud.vision import types

vision_client = vision.ImageAnnotatorClient('account_key.json')

x = 1000
z=".jpg"

while True:
	try:
		file_name_base = "twitterimage"
		y = str(x)
		x = x+1
		file_name = file_name_base + y + z
		with io.open(file_name, 'rb') as image_file:
			content = image_file.read()
			image = vision.types.Image(content=content)

		response = vision_client.label_detection(image=image)
		labels = response.label_annotations
		r = x-1000
		print("description of photo ",r,": ")
		for label in labels:
			print(label.description)
	except:
		break

