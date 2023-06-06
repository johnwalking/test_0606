# Install 
1. pip install mtcnn
2. pip install dlib

# Function introduce

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