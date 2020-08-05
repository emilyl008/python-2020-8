f_copy = open('image.png','rb')
img = f_copy.read()
f_copy.close()

copy = open('copy.png','wb')
copy.write(img)
copy.close()