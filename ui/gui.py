import sys
from PyQt4 import QtGui,QtCore
from manager_ui import Ui_MainWindow
from popups import add_person_popup

class gui(QtGui.QMainWindow,Ui_MainWindow):
    
    create_popup_signal = QtCore.pyqtSignal(object)
    resize_signal = QtCore.pyqtSignal()
    enable_signal = QtCore.pyqtSignal(object,object) 
    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    
        self.create_popup_signal.connect(self.createPopup)        
        self.enable_signal.connect(self.signal_enable)
        self.add_person_btn.clicked.connect(self.add_person_cb)
        
    def createPopup(self,popup):
        popup(parent = self)
        
    def add_person_cb(self):
        self.create_popup_signal.emit(add_person_popup)
    
    def signal_enable(self,widget,enable):
        widget.setEnabled(enable)
            
    def resizeEvent(self, *args, **kwargs):
        self.resize_signal.emit()
        return QtGui.QMainWindow.resizeEvent(self, *args, **kwargs)
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    
    
    sys.exit(app.exec_())