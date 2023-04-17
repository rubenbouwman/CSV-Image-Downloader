from pandas import *
import requests

# Reading CSV file
data = read_csv("CSV Files/Decathlon-product-reviews.csv")

# converting column data to list
Images = data['Img'].tolist()

# Method to download all images from the links in the list
def imageDownloader():
    for imageURL in Images:
        response = requests.get(imageURL).content
        filename = imageURL.split('/')[-1]
        with open('Images/' + filename, 'wb') as handler:
            handler.write(response)

imageDownloader()
