import os

installCOmmand = f'''
!pip install torch
!pip install torchvision
!pip install opencv-python
!pip install scipy-image
!pip install scipy
!pip install Pillow
!pip install google-colab
'''
commandList = installCOmmand.split('!')

for com in commandList:
    print(f'[INFO] Executing {com}')
    os.system(str(com))