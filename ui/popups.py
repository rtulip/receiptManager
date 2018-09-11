from PyQt4 import QtGui,QtCore
from base_popup import Ui_Frame

class popup(Ui_Frame,QtGui.QFrame):
    
    def __init__(self,parent = None):
        Ui_Frame.__init__(self)
        QtGui.QFrame.__init__(self,parent = parent)
        self.setupUi(self)
        self.margin = 50
        self.parent = parent
        self.parent.resize_signal.connect(self.resize_to_parent)
        self.parent.enable_signal.emit(self.parent.centralwidget,False)
        self.resize_to_parent()
        self.pushButton.clicked.connect(self.exit)
        self.destroyed.connect(self.confirm_destroy)
        self.show()
        
    def exit(self):
        self.deleteLater()
        self.parent.resize_signal.disconnect()
        self.hide()
        self.parent.enable_signal.emit(self.parent.centralwidget,True)
    
    def confirm_destroy(self):
        print "Destroyed popup"   
    
    def resize_to_parent(self):
        
        self.setGeometry(QtCore.QRect(self.parent.x() + self.margin,
                                      self.parent.y() + self.margin,
                                      self.parent.width() - self.margin * 4,
                                      self.parent.height() - self.margin * 4))
        
        
class add_person_popup(popup):
    
    def __init__(self, parent = None):
        popup.__init__(self,parent)
                
if __name__ == '__main__':
    app = QtGui.QApplication([])
    
    test = add_person_popup(None)
    
    app.exec_()