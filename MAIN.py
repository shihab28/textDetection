import os
import shutil
import RESIZE_IMAGES as reimg
import time


imageDir = r'E:\DATA_ANL - Copy\textDetection\resource\formatted_image'
rawimageDir = r'E:\DATA_ANL - Copy\textDetection\resource\raw_image'
# cmdFormat = f'python text_detection.py --image images/lebron_james.jpg --east frozen_east_text_detection.pb'

def startDectecting(imageDir):
    global startTime
    curScriptDIr = os.path.dirname(__file__)

    imageDir = str(imageDir).replace('\\', '/')
    curScriptDIr = str(curScriptDIr).replace('\\', '/')
    
    scirptPath = f'{curScriptDIr}/MAIN_DETECT.py'
    eastPbPath = f'{curScriptDIr}/frozen_east_text_detection.pb'
    imgList = os.listdir(imageDir)

    rootDir, imdname = os.path.split(imageDir)
    boxedDir = f'{rootDir}/boxed_image'
    if os.path.isdir(boxedDir):
        shutil.rmtree(boxedDir)        
    os.makedirs(boxedDir)

    tempStartTime = startTime
    for img in imgList:
        imgPath = f'{imageDir}/{img}'

        command = f"python \"{scirptPath}\" --image \"{imgPath}\" --east \"{eastPbPath}\" &"
        # print('Command : ', command)
        os.system(command)
        tempEndTime = time.time()
        print(f"[INFO] ({img}) text detection took {round((tempEndTime - tempStartTime), 4)} Seconds")
        tempStartTime = tempEndTime


def main_function(imageDir=None, rawImageDir = None):
    global startTime
    startTime = time.time()
    
    if imageDir != None:
        if os.path.exists(imageDir):
            startDectecting(imageDir)

    elif rawImageDir != None:
        print('Resizing images')
        if os.path.exists(rawImageDir):
            imageDir = reimg.main_function(rawFolderDir=rawImageDir,  size = (320, 320))
            startDectecting(imageDir)
             
    else:
        print("Couldn't Do the Op")  

    endTime = time.time()
    print(f"[INFO] total detection took {round((endTime - startTime), 4)} Seconds")      


main_function(imageDir=imageDir)





