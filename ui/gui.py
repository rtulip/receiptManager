from PyQt4 import QtGui,QtCore
from manager_ui import Ui_MainWindow
from popups import add_person_popup

class gui(QtGui.QMainWindow,Ui_MainWindow):
    
    create_popup_signal = QtCore.pyqtSignal(object)
    resize_signal = QtCore.pyqtSignal()
    enable_signal = QtCore.pyqtSignal(object,object) 
    def __init__(self,manager):
        self.manager = manager
        QtGui.QWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    
        self.create_popup_signal.connect(self.create_popup)        
        self.enable_signal.connect(self.signal_enable)
        self.add_person_btn.clicked.connect(self.add_person_cb)
        self.update_display()
        
    def create_popup(self,popup):
        popup(parent = self)
        
    def add_person_cb(self):
        self.create_popup_signal.emit(add_person_popup)
    
    def signal_enable(self,widget,enable):
        widget.setEnabled(enable)
            
    def resizeEvent(self, *args, **kwargs):
        self.resize_signal.emit()
        return QtGui.QMainWindow.resizeEvent(self, *args, **kwargs)
    
    def update_display(self):
        string_list = "People: \n"
        for name,values in self.manager.persons.iteritems():
            string_list += name+": Owes: "+str(values["Owes"])+"\n"
        self.label.setText(string_list)
            