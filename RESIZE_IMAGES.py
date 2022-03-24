import cv2
import os
import shutil


rawFolderDir = r'E:\DATA_ANL - Copy\textDetection\resource\raw_image'
rawImageDir = None


def main_function(rawFolderDir = None, rawImageDir = None, size = (320, 320)):

    if rawFolderDir != None and rawImageDir == None :
        imageDirList = os.listdir(rawFolderDir)

        rootDir, folderName = os.path.split(rawFolderDir)
        formatDir = f'{rootDir}/formatted_image'
        
        if os.path.isdir(formatDir):
            shutil.rmtree(formatDir)        
        os.makedirs(formatDir)

        if imageDirList != []:
            for i, imgName in enumerate(imageDirList):
                imgFolderDir, imageName = rawFolderDir, imgName
                tempImg = cv2.imread(f'{imgFolderDir}/{imageName}', cv2.IMREAD_UNCHANGED)
                resizedImg = cv2.resize(tempImg, size, interpolation=cv2.INTER_NEAREST)
                cv2.imwrite(f'{formatDir}/{imgName}',resizedImg)
    
    return formatDir
    

if __name__ == '__main__':
    size = (320, 320)
    main_function(rawFolderDir=rawFolderDir, size=size)

