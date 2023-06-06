# Dataset introduce
1. side: 側臉
2. front_side: 正側臉
3. front: 正臉
4. not_person: 非人臉

# Install 
1. pip install mtcnn
2. pip install dlib

# Function introduce

在辨識側臉的過程中，發現mtcnn效果不太好，所以加入dlib的人臉辨識，提高辨識效果，只有在兩個模型都無法辨識為人臉時才判斷為沒有人臉。

##  1-1 detectHumanFaceExist
check if the human face exists in the input image and return True or False

## 1-2 cropHumanFaceArea
Purpose : crop the human face area and store it.
parameter:
1. img: input image
2. choice: choose from ['head' 'chest' 'waist' 'customized']
3. if choice is setting with 'customized', the w_ratio and h_ratio need to be assigned  with number to achieve the target, .
4. store_loc: to assign where to store the image

## 1-3 checkResolution
1. check if the cropped image achieve the resoltuion limit.
2. return True or False

# Exexute
python3 main.py
