
import os
import Desc
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
import matplotlib.pyplot as plt

cog_key = 'b73d013ef8484ba09c329494e968f894'
cog_endpoint = 'https://cotr.cognitiveservices.azure.com/'

# Get a client for the computer vision service
computervision_client = ComputerVisionClient(
    cog_endpoint, CognitiveServicesCredentials(cog_key))

# Get the path to an image file
image_path = os.path.join('data', 'iron.jpg')

# Specify the features we want to analyze
features = ['Description', 'Tags', 'Adult', 'Objects', 'Faces']

# Get an analysis from the computer vision service
image_stream = open(image_path, "rb")
analysis = computervision_client.analyze_image_in_stream(
    image_stream, visual_features=features)

# Show the Caption of the Image (code in vision.py)
Desc.show_image_analysis(image_path, analysis)
