from PyQt4 import QtGui,QtCore
from base_popup import Ui_Frame

class popup(Ui_Frame,QtGui.QFrame):
    
    def __init__(self,parent = None,title = None):
        Ui_Frame.__init__(self)
        QtGui.QFrame.__init__(self,parent = parent)
        self.setupUi(self)
        if title:
            self.title_label.setText(title)
        self.percent = 0.75
        self.parent = parent
        self.parent.resize_signal.connect(self.resize_to_parent)
        self.parent.enable_signal.emit(self.parent.centralwidget,False)
        self.resize_to_parent()
        self.pushButton.clicked.connect(self.exit)
        self.show()
        
    def exit(self):
        self.deleteLater()
        self.parent.resize_signal.disconnect()
        self.hide()
        self.parent.enable_signal.emit(self.parent.centralwidget,True)
    
    def resize_to_parent(self):
        
        self.setGeometry(QtCore.QRect(self.parent.width()*((1-self.percent)/2),
                                      self.parent.height()*((1-self.percent)/2),
                                      self.percent*self.parent.width(),
                                      self.percent*self.parent.height()))
        
        
class add_person_popup(popup):
    
    def __init__(self, parent = None):
        popup.__init__(self,parent,"Add New Person")
        vertical_layout = QtGui.QVBoxLayout()
        horizontal_layout = QtGui.QHBoxLayout()
        self.text_label = QtGui.QLabel()
        self.text_label.setText("Enter Name: ")
        self.text_field = QtGui.QTextEdit()
        self.text_field.setSizePolicy(QtGui.QSizePolicy(
                                        QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum))
        horizontal_layout.addWidget(self.text_label)
        horizontal_layout.addWidget(self.text_field)
        
        self.ok_button = QtGui.QPushButton("OK")
        vertical_layout.addItem(horizontal_layout)
        vertical_layout.addItem(QtGui.QSpacerItem(10,
                                                  10,
                                                  QtGui.QSizePolicy.Expanding,
                                                  QtGui.QSizePolicy.Expanding))
        vertical_layout.addWidget(self.ok_button)
        self.groupBox.setLayout(vertical_layout)
        
        self.ok_button.clicked.connect(self.add_person)
        
        self.show()
        
    def add_person(self):
        if self.text_field.toPlainText() not in self.parent.manager.persons:
            self.parent.manager.persons[str(self.text_field.toPlainText())] = {"Owes":0,"Transactions": {}}
            print self.parent.manager.persons
            self.parent.update_display()
        self.exit()

class add_receipt_popup(popup):
    
    def __init__(self,parent = None):
        popup.__init__(self, parent)
        
        self.groupBox.deleteLater()
        self.groupBox.hide()
        
        self.scroll_area = QtGui.QScrollArea()
        self.ok_button = QtGui.QPushButton("OK")
        self.verticalLayout.addWidget(self.scroll_area)
        self.verticalLayout.addWidget(self.ok_button)
        self.scroll_area_layout = QtGui.QVBoxLayout()
        
        self.scroll_area_layout.addItem(QtGui.QSpacerItem(10,
                                                  10,
                                                  QtGui.QSizePolicy.Expanding,
                                                  QtGui.QSizePolicy.Expanding))
        self.scroll_area.setLayout(self.scroll_area_layout)
        self.show()
        
    def spawn_item_area(self):
        pass
        
        
if __name__ == '__main__':
    app = QtGui.QApplication([])
    
    test = add_person_popup(None)
    
    app.exec_()