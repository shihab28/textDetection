import os

curDir = os.path.dirname(__file__)

scriptPath = f"{curDir}/pipeline.py"
modelPath = f"{curDir}/model/craft_mlt_25k"
testFolderPath = f"{curDir}/test_folder"


command = f'''
python \"{scriptPath}\" --trained_model=\"{modelPath}\" --test_folder=\"{testFolderPath}\""
'''

os.system(command)