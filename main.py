import os
import cv2
import mtcnn
import dlib

DATA_FOLDER = './Data/'

# initialize the model MTCNN
detector_mtcnn = mtcnn.MTCNN()
# initialize model from dlib
detector_dlib = dlib.get_frontal_face_detector()

# check if image contains the human face
def detectHumanFaceExist(img) -> bool:
  faces = detector_mtcnn.detect_faces(img)
  face_rects, scores, idx = detector_dlib.run(img, 0)
  # print(faces)
  if len(faces) ==0 and len(scores) ==0:
    return False
  else:
    return True
# check the crop area can fit the image size
def checkSize(x1,y1,w,h, w_ratio, h_ratio, img_h, img_w):
  if (x1 - w*(w_ratio-1)/2) <0 or (int(x1+(w+w*w_ratio)/2))>=img_w or(int(y1+h_ratio*h)>=img_h):
      return False
  else:
    return True
  
# crop the area contain human face
def cropHumanFaceArea(img, choice, w_ratio=1.0, h_ratio=1.0, store_loc='./tmp.jpg'):
  img_h, img_w = len(img), len(img[0])
  # print(img_h, img_w)
  faces = detector_mtcnn.detect_faces(img)
  if len(faces) >0:
    for face in faces:
      (x, y, w, h) = face['box']
      y1,y2,x1,x2 = y, y+h, x, x+w
  else:
    face_rects, _, _ = detector_dlib.run(img, 0)
    for rect in face_rects:
      x1,y1,x2,y2 = rect.left(),rect.top(),rect.right(),rect.bottom()
      h,w =y2-y1, x2 - x1
  
  if choice == 'head':
    w_ratio = 1
    h_ratio = 1
  elif choice == 'chest':
    w_ratio = 2.2
    h_ratio = 2
  elif choice == 'waist':
    w_ratio = 2.2
    h_ratio = 3.5
  elif choice == 'customized':
    w_ratio = w_ratio
    h_ratio = h_ratio

  if checkSize(x1, y1, w, h, w_ratio, h_ratio,img_h, img_w):
    # print(y1, y1+h_ratio*h, x1-w*(w_ratio-1)/2, x1+(w+(w*w_ratio))/2)
    crop_img = img[y1:int(y1+h_ratio*h), int(x1-w*(w_ratio-1)/2):int(x1+(w+(w*w_ratio))/2)]
    cv2.imwrite(store_loc,crop_img)
    print("store successfully.")
  else:
    print("No enough space for cropping ")

def checkResolution(img, thres_H, thres_W):
  img_h, img_w = len(img), len(img[0])
  # print(img_h, img_w)
  if img_h< thres_H or img_w < thres_W:
    return False
  return True

if __name__=='__main__': 
  # 1-1 test the function whether human face exists
  results = []
  for folder_name in sorted(os.listdir(DATA_FOLDER)):
    if folder_name  == '.DS_Store':
      continue
    for file in sorted(os.listdir(os.path.join(DATA_FOLDER, folder_name))):
      if file =='.DS_Store':
        continue
      print(os.path.join(DATA_FOLDER, folder_name, file))
      img = cv2.imread(os.path.join(DATA_FOLDER, folder_name, file))
      result = detectHumanFaceExist(img)
      results.append(result)
  print(results)
  assert results == [True]*10+ [False]*5+[True]*5

  ## test crop function
  img = cv2.imread(os.path.join(DATA_FOLDER, 'front', '1.jpg'))
  result = cropHumanFaceArea(img, 'head', store_loc='./head.jpg')
  result = cropHumanFaceArea(img, 'chest', store_loc='./chest.jpg')
  result = cropHumanFaceArea(img, 'waist', store_loc= './waist.jpg')
  result = cropHumanFaceArea(img, 'customized', 3.0,3.0,store_loc= './custom.jpg')
  result = cropHumanFaceArea(img, 'customized', 6.0,6.0,store_loc= './custom2.jpg')
  ## test check resolution
  img = cv2.imread('./chest.jpg')
  result = checkResolution(img, 500, 500)
  print(result)
  result = checkResolution(img, 300, 300)
  print(result)

