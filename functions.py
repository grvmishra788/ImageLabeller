from PyQt5.QtGui import QPixmap
import variables
import os
import shutil

def loadImage(previewLabel):
    path = variables.IMAGE_LIST[variables.CURR_PREVIEW_INDEX]
    image = QPixmap(path)
    previewLabel.setPixmap(image)


# action method
def clickMe(labelOutput, previewLabel):
    output = f"The source location has {len(variables.IMAGE_LIST)} images"
    labelOutput.setText(output)
    if len(variables.IMAGE_LIST) > 0:
        loadImage(previewLabel)
    else:
        previewLabel.setText("No images available!")

def clickPrev(previewLabel):
    variables.CURR_PREVIEW_INDEX -= 1
    while not os.path.exists(variables.IMAGE_LIST[variables.CURR_PREVIEW_INDEX]):
        variables.CURR_PREVIEW_INDEX -= 1
    loadImage(previewLabel)

def clickNext(previewLabel):
    variables.CURR_PREVIEW_INDEX = (variables.CURR_PREVIEW_INDEX + 1) % variables.TOTAL_IMAGES
    while not os.path.exists(variables.IMAGE_LIST[variables.CURR_PREVIEW_INDEX]):
        variables.CURR_PREVIEW_INDEX = (variables.CURR_PREVIEW_INDEX + 1) % variables.TOTAL_IMAGES
    loadImage(previewLabel)

def clickSave(previewLabel):
    src_path = variables.IMAGE_LIST[variables.CURR_PREVIEW_INDEX]
    if variables.CURR_SELECTED_LABEL_INDEX < 0 or variables.DEST_DIR == "":
        return
    dest_folder = os.path.join(variables.DEST_DIR, variables.LABEL_LIST[variables.CURR_SELECTED_LABEL_INDEX])
    if variables.CURR_SELECTED_LABEL_INDEX == len(variables.LABEL_LIST) - 1 and variables.OTHER_CATEGORY_LABEL != "":
        dest_folder = os.path.join(dest_folder, variables.OTHER_CATEGORY_LABEL)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    file_name = src_path.split("\\")[-1]
    dest_path = os.path.join(dest_folder, file_name)
    shutil.move(src_path, dest_path)
    clickNext(previewLabel)

def clickRadioButton(index):
    variables.CURR_SELECTED_LABEL_INDEX = index