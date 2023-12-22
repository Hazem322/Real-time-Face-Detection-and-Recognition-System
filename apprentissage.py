import cv2,os
import numpy as np
import PIL
from PIL import Image
recognizer=cv2.face.createLBPHFaceRecognizer()
#recognizer=cv2.createLBPHFaceRecognizer()
#recognizer=cv2.createLBPHFaceRecognizer()
#recognizer=cv2.face.LBPHFaceRecognizer_create() 
path= 'dataSet'
def getImagesWithID(path) :
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths :
        faceImg=Image.open(imagePath).convert('L') ;
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath) [-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow('training',faceNp)
        cv2.waitKey(10)
    return IDs,faces
IDs,faces=getImagesWithID(path)
recognizer.train(faces,np.array(IDs))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
