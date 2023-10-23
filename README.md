# Object Detection using Pytorch

>Initially install all the libraries in the local machine 

you should install the Libraries Like :
```
import torch
import torchvision
from torchvision import transforms as T
import cv2
import cvzone
import sys
```

Else just install the `requirement.txt`

```
pip install -r requirements.txt
```

> To run the `code`

```
py main.py [image_name.extension]
```

Or you can try with the given images in the repo
```
py main.py image1.jpg
```

> now lets discuss about the code 

Basically we considered the pretrained model `ssd300_vgg16` as you can see in the code
```
model = torchvision.models.detection.ssd300_vgg16(pretrained = True)
```
By the help of CV2 we read the image and convert it to thhe tensor and then pridict the values based on the scores of the tensor and consider the bbox for the score value `above 60%` and detect it and draw a box on it and lable it with `cvzone`

> The input images are 

![image1](https://github.com/udaychandp/PyTorch_Object_detection/assets/114306402/42ead510-69bc-4a9f-9401-28491e102181)

![image2](https://github.com/udaychandp/PyTorch_Object_detection/assets/114306402/3fb48f91-1e1a-4bee-a6d3-e685d26fe764)

![image3](https://github.com/udaychandp/PyTorch_Object_detection/assets/114306402/24ada51f-8282-4756-bd04-3ecf391c914a)

> Lets see the results of them

![image2_result](https://github.com/udaychandp/PyTorch_Object_detection/assets/114306402/134981ac-bdea-4874-b7c8-b5b890fc254e)

![image1_result](https://github.com/udaychandp/PyTorch_Object_detection/assets/114306402/c63e947e-f70e-4538-b4a5-82bbdd1f497a)

![Untitled](https://github.com/udaychandp/PyTorch_Object_detection/assets/114306402/d93e83c1-1c28-430f-8ab2-53526d772867)










