from quicklaunch import Ui_QuickLaunch
from time import sleep
from PyQt5.QtCore import *

def test_myapp(qtbot):
    window = Ui_QuickLaunch.setupUi()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitForWindowShown(window)
    sleep(3)
    qtbot.mouseClick(window.buttonBox.buttons()[0], Qt.LeftButton)
    assert window.label.text() == 'accept'
    qtbot.stopForInteraction()