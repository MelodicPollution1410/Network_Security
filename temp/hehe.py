import sys
import os
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtCore import QProcess

app = QApplication(sys.argv)

box = QMessageBox()
box.setText("Text")
box.show()

def on_readyReadStandardOutput():
    print(process.readAllStandardOutput().data().decode(), end="")

process = QProcess()
process.start("ping", ["8.8.8.8"])
process.readyReadStandardOutput.connect(on_readyReadStandardOutput)
sys.exit(app.exec_())