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
    # -----------------

    # Or

    # Get objects
    if analysis.objects:
        # Draw a rectangle around each object
        for object in analysis.objects:
            r = object.rectangle
            bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)
            plt.annotate(object.object_property, (r.x, r.y),
                         backgroundcolor='magenta')

    # ------------------

    # Or

    # Get faces
    if analysis.faces:
        # Draw a rectangle around each face
        for face in analysis.faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top),
                            (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='lightgreen', width=5)
            annotation = 'Person aged approxilately {}'.format(face.age)
            plt.annotate(annotation, (r.left, r.top),
                         backgroundcolor='lightgreen')

    # ------------------

    # Remove the Axes and Show the image
    plt.axis('off')
    plt.imshow(img)

    plt.show()
