import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import paramiko
from PyQt5.QtCore import QObject,QProcess

import sshcmd  
import device_count 
import os 
import sys


class sniffing(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("sniffer.ui",self)
        self.sniff.clicked.connect(self.anomaly_detection)
        self.stop.clicked.connect(self.detection_stop)
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self._pid = -1

    @QtCore.pyqtSlot()
    def anomaly_detection(self):
        self.textEdit.clear()
        
        self.Infterface=self.interface_2.text()
        #self.textEdit.setText("Starting IDS...")
        #self.process.setProgram("sudo snort -A console -q -u snort -g snort -c /etc/snort/snort.conf -i "+self.etherNetInfterface)
        #cmd="ping"
        #cmd1="8.8.8.8"
        #self.process.setProgram(cmd)
        #self.process.setArguments(cmd1)
        #
        #self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        #self.process.start()
        #self.process.kill()
        #args = (["-A","console","-q","-u","snort","-g","snort","-c","/etc/snort/snort.conf","-i","enp2s0"])
        #runstr ="snort"
        #List arguments()
        args=(["-v","-i",self.Infterface])
        runstr="snort"
        #self.args=["localhost"]
        self.process.setProgram(runstr)
        self.process.setArguments(args)
        self.process.start()
        #print(ok)
        #if ok:
        #    self._pid = pid
        #parent = QObject()            
        #program = "ping"        
        ##arguments = QStringList()
        #arguments=(["localhost"])
        #myProcess = QProcess(parent)
        #myProcess.start(program, arguments)

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        #text=self.process.readAllStandardOutput().data().decode()
        #print(text)
        self.textEdit.append(self.process.readAllStandardOutput().data().decode())

    @QtCore.pyqtSlot()
    def detection_stop(self):
        #if self._pid > 0:
        #    p = psutil.Process(self._pid)
        #    p.kill()
        #    self._pid = -1
        self.process.kill()


class anamoly(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("anomaly.ui",self)
        self.detection.clicked.connect(self.anomaly_detection)
        self.stop_2.clicked.connect(self.detection_stop)
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self._pid = -1


    @QtCore.pyqtSlot()
    def anomaly_detection(self):
        self.textEdit.clear()
        
        self.etherNetInfterface=self.ether.text()
        self.timee=self.time.text()
        self.timee=self.timee+"s"
        #self.textEdit.setText("Starting IDS...")
        #self.process.setProgram("sudo snort -A console -q -u snort -g snort -c /etc/snort/snort.conf -i "+self.etherNetInfterface)
        #cmd="ping"
        #cmd1="8.8.8.8"
        #self.process.setProgram(cmd)
        #self.process.setArguments(cmd1)
        #
        #self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        #self.process.start()
        #self.process.kill()
        #args = (["-A","console","-q","-u","snort","-g","snort","-c","/etc/snort/snort.conf","-i","enp2s0"])
        #runstr ="snort"
        #List arguments()
        args=([self.timee,"snort","-A","console","-q","-c","/etc/snort/snort.conf","-i",self.etherNetInfterface])
        runstr="timeout"
        #self.args=["localhost"]
        self.process.setProgram(runstr)
        self.process.setArguments(args)
        self.process.start()
        #print(ok)
        #if ok:
        #    self._pid = pid
        #parent = QObject()            
        #program = "ping"        
        ##arguments = QStringList()
        #arguments=(["localhost"])
        #myProcess = QProcess(parent)
        #myProcess.start(program, arguments)




    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        text=self.process.readAllStandardOutput().data().decode()
        #print(text)
        if(text==None or text == ''):
            self.textEdit.append("NO ANOMALY FOUND")
        else:
            self.textEdit.append(text)

    @QtCore.pyqtSlot()
    def detection_stop(self):
        #if self._pid > 0:
        #    p = psutil.Process(self._pid)
        #    p.kill()
        #    self._pid = -1
        self.process.terminate()

    


class detect_sniffer(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("sniffer_detect.ui",self)
        self.sbmt.clicked.connect(self.on_sshClickedwire)
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)

    @QtCore.pyqtSlot()
    def on_sshClickedwire(self):
        self.textEdit.clear()
        self.user=self.le1.text()
        self.ip=self.le2.text()
        self.passwordd=self.le3.text()
        self.cmdd="ps -e | grep "+self.sname.text()
        if(self.user=='' or self.user== None and self.ip=='' or self.ip== None and self.passwordd=='' or self.passwordd== None and self.cmdd=='' or self.cmdd== None):
            self.textEdit.clear()
            self.textEdit.append("Please enter the valid info")
        else:
            #print(self.cmdd)
            var=sshcmd.ssh_cmd(self.user,self.ip,self.passwordd,self.cmdd)
            self.textEdit.append(var)
        

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.textEdit.append(text)

    @QtCore.pyqtSlot()
    def on_finished(self):
        self.button.setText("Start")

class netDevice_scan(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("device_scan.ui",self)
        self.sbmt.clicked.connect(self.device_scan)
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)
        #print(self.cmd)


    @QtCore.pyqtSlot()
    def device_scan(self):
        self.textEdit.clear()
        self.ipadr=self.ip.text()

        if(self.ipadr=='' or self.ip== None):
            self.textEdit.clear()
            self.textEdit.append("Please enter the enter the valid info ")
        else:
            var1,var2=device_count.capture(self.ipadr)
            self.textEdit.append('Number of devices in the network: '+ var1)
            self.textEdit.append('Device details: ')
            #print(var1)
            for i in var2:
                self.textEdit.append(i)

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.textEdit.append(text)

    @QtCore.pyqtSlot()
    def on_finished(self):
        self.button.setText("Start")

class ssh_cmd(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ssh_cmd.ui",self)
        self.excu.clicked.connect(self.on_sshClicked)
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)


    @QtCore.pyqtSlot()
    def on_sshClicked(self):
        self.textEdit.clear()
        self.user=self.le1.text()
        self.ip=self.le2.text()
        self.passwordd=self.le3.text()
        self.portt=self.port.text()
        self.cmdd=self.cmd.text()

        if(self.portt==' ' or self.portt==None):
            self.portt="22"

        if(self.user=='' or self.user== None and self.ip=='' or self.ip== None and self.passwordd=='' or self.passwordd== None and self.cmdd=='' or self.cmdd== None):
            self.textEdit.clear()
            self.textEdit.append("Please enter the valid info")
        else:
            print(self.cmdd)
            var=sshcmd.ssh_cmd(self.user,self.ip,self.passwordd,self.cmdd,self.portt)
            self.textEdit.append(var)

        

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.textEdit.append(text)

    @QtCore.pyqtSlot()
    def on_finished(self):
        self.button.setText("Start")

class Widget(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("main.ui",self)
        self.w= detect_sniffer()
        self.v=netDevice_scan()
        self.x=ssh_cmd()
        self.y=anamoly()
        self.z=sniffing()
        #self.button.clicked.connect(self.on_clicked)
        self.process = QtCore.QProcess(self)

        self.dec.clicked.connect(self.show_detect)
        self.dvscan.clicked.connect(self.show_device_scan)
        self.ssh.clicked.connect(self.show_ssh_cmd)
        self.amly.clicked.connect(self.show_anamoly_detection)
        self.sniffer.clicked.connect(self.show_sniffing)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        self.cmdd=self.cmd.text()
        print(self.cmdd)
        self.process.setProgram(self.cmdd)
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        if self.button.text() == "Start":
            self.textEdit.clear()
            self.textEdit.setText("Starting IDS...")
            self.textEdit.append("$:")
            #self.process.setArguments([self.lineedit.text()])
            self.process.start()
            #self.button.setText("Stop")
        #elif self.button.text() == "Stop":
         #   self.process.kill()
         #   self.textEdit.append("Process killed")
    def on_clicked_stop(self):
        self.process.kill()
        self.textEdit.append("Process killed")

    def show_detect(self, checked):
        self.w.show()
        
    def show_device_scan(self):
        self.v.show()
    
    def show_ssh_cmd(self):    
        self.x.show()

    def show_anamoly_detection(self):
        self.y.show()

    def show_sniffing(self):
        self.z.show()

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.textEdit.append(text)

    @QtCore.pyqtSlot()
    def on_finished(self):
        self.button.setText("Start")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Widget()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(842)
    widget.setFixedHeight(553)
    widget.show()
    app.exec_()    