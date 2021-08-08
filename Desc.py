import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np


def show_image_analysis(image_path, analysis):

    # Display the image
    fig = plt.figure(figsize=(16, 8))
    a = fig.add_subplot(1, 2, 1)
    img = Image.open(image_path)

    # Get the caption
    caption_text = ''
    if (len(analysis.description.captions) == 0):
        caption_text = 'No caption detected'
    else:
        for caption in analysis.description.captions:
            caption_text = caption_text + \
                " '{}'\n(Confidence: {:.2f}%)".format(
                    caption.text, caption.confidence * 100)
    plt.title(caption_text)

    # Remove the Axes and Show the image
    plt.axis('off')
    plt.imshow(img)

    plt.show()
