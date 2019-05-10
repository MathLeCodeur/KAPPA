import os
import shutil
import yaml

from PyQt5.QtWidgets import QApplication

configPath = os.path.join('res', 'config', 'config.yaml')

__loaded = False
__configMap = {}

def __load():
    global __configMap

    with open(configPath, 'r') as configFile:
        __configMap = yaml.safe_load(configFile)

def get(key: str):
    global __configMap

    if not __loaded:
        __load()

    return __configMap[key]

def set(key: str, value: str):
    global __configMap

    if not __loaded:
        __load()

    __configMap[key] = value

    with open(configPath, 'w') as configFile:
        yaml.dump(__configMap, configFile)

def loadThemes(app: QApplication, iconsChanged: bool):
    with open(os.path.join('res', 'styles', 'common.css'), 'r') as commonStyleSheetFile:
        with open(os.path.join('res', 'styles', 'themes', get('theme'), get('theme') + '_theme.css'), 'r') as themeStyleSheetFile:
            app.setStyleSheet(commonStyleSheetFile.read() + '\n' + themeStyleSheetFile.read())

    if iconsChanged:
        iconsDir = os.path.join('res', 'icons')

        iconsCacheDir = os.path.join(iconsDir, 'cache')
        for iconFile in os.listdir(iconsCacheDir):
            os.remove(os.path.join(iconsCacheDir, iconFile))

        iconsThemeDir = os.path.join(iconsDir, get('iconTheme'))
        for iconFile in os.listdir(iconsThemeDir):
            shutil.copyfile(os.path.join(iconsThemeDir, iconFile), os.path.join(iconsCacheDir, iconFile))
