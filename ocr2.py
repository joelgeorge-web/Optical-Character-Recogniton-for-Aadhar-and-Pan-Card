import easyocr
reader = easyocr.Reader(['en'], gpu=False) # this needs to run only once to load the model into memory
# result = reader.readtext('aadhar.jpg')
# print(result)
image = 'aadhar.jpg'
result = reader.readtext(image)

for detection in result:
    text = detection[1]
    print(text)

