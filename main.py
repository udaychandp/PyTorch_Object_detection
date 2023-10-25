import torch
import torchvision
from torchvision import transforms as T
import cv2
import sys


model = torchvision.models.detection.ssd300_vgg16(pretrained = True)
model.eval()

classnames = []
with open('classes.txt','r') as f:
    classnames = f.read().splitlines()


image = cv2.imread(sys.argv[1])
img = image.copy()
print(type(image))

imgtransform = T.ToTensor()
image = imgtransform(image)
print(type(image))

with torch.no_grad():
    ypred = model([image])
    print(ypred[0].keys())

    bbox,scores,labels = ypred[0]['boxes'],ypred[0]['scores'],ypred[0]['labels']
    nums = torch.argwhere(scores > 0.60).shape[0]
    font = cv2.FONT_HERSHEY_DUPLEX
    for i in range(nums):
        x,y,w,h = bbox[i].numpy().astype('int')
        alfa = cv2.rectangle(img,(x,y),(w,h),(0,0,255),2)
        classname = labels[i].numpy().astype('int')
        classdetected = classnames[classname-1]
        img1 = cv2.putText(alfa,classdetected,(x,y-10),font,1,(0,0,255),1,cv2.LINE_AA)

cv2.imshow('Detection',img)
cv2.waitKey(0)