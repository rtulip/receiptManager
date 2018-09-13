from PyQt4 import QtGui
from ui.gui import gui
import sys
import json
import os

class manager():
    
    def __init__(self):
        
        self.save_path = "/home/robbie/Documents/receipts/"
        self.people_path = self.save_path + 'people.txt'
        self.receipt_path = self.save_path + "receipt_history.txt"   
        self.persons = {}
        self.receipts = {}
        
        if os.path.exists(self.save_path):
            if os.path.exists(self.people_path):
                with open(self.people_path,"r") as fp:
                    self.persons = json.load(fp)
            if os.path.exists(self.receipt_path):
                with open(self.receipt_path,"r") as fp:
                    self.receipts = json.load(fp)
        self.ui = gui(self)
        self.ui.show()
    
    def exit(self):
        print "Exiting"
        if not os.path.exists(self.save_path):
            try:
                os.mkdir(self.save_path)
            except Exception as e:
                "Failed to make save path",e
        
        try:
            with open(self.people_path, "w") as fp:
                json.dump(self.persons,fp,indent = 4, sort_keys = True)
            
            with open(self.receipt_path,"w") as fp:
                json.dump(self.receipts,fp,indent = 4, sort_keys = True)
                
        except Exception as e:
            print "Failed to save file", e

def exit_program():
    app.exec_()
    man.exit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    man = manager()
    
    sys.exit(exit_program())