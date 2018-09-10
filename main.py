from PyQt4 import QtGui
from ui.gui import gui
import sys

class manager():
    
    def __init__(self):
        self.persons = {}
        self.receipts = {}
        
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    manager = manager()
    
    ui = gui()
    ui.show()
    
    sys.exit(app.exec_())