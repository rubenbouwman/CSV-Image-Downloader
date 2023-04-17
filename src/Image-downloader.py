from pandas import *

# Reading CSV file
data = read_csv("CSV Files/Decathlon-product-reviews.csv")

# converting column data to list
Images = data['Img'].tolist()
Review = data['Review'].tolist()

print(Images)
