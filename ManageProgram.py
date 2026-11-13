from PySide6.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PasswordManage_design import Ui_Dialog
import sys
import json

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.TheListOfPasswords.setColumnCount(2)
        self.ui.TheListOfPasswords.setHorizontalHeaderLabels(["Сайт", "Пароль"])
        self.ui.AddPasswordQt.clicked.connect(self.addPas)
        self.loadd()
    def addPas(self):
        self.siteText = self.ui.writePasswordbu.text()
        self.passw = self.ui.writeSite.text()
        if not self.siteText or not self.passw:
            return
        self.row = self.ui.TheListOfPasswords.rowCount()
        self.ui.TheListOfPasswords.insertRow(self.row)
        self.ui.TheListOfPasswords.setItem(self.row, 0 , QTableWidgetItem(self.passw))
        self.ui.TheListOfPasswords.setItem(self.row, 1 , QTableWidgetItem(self.siteText))
        self.ui.writePasswordbu.clear()
        self.ui.writeSite.clear()
        self.save()
    def loadd(self):
     try:
        with open("passwords.json", "r", encoding='UTF-8') as file:
            data = json.load(file)
        for site, passwo in data.items():
            self.row = self.ui.TheListOfPasswords.rowCount()
            self.ui.TheListOfPasswords.insertRow(self.row)
            self.ui.TheListOfPasswords.setItem(self.row, 0 , QTableWidgetItem(passwo))
            self.ui.TheListOfPasswords.setItem(self.row, 1 , QTableWidgetItem(site))
     except Exception as e:
         return
    def save(self):
        data = {}
        for i in range(self.ui.TheListOfPasswords.rowCount()):
            item_site = self.ui.TheListOfPasswords.item(i, 0)
            item_passwo = self.ui.TheListOfPasswords.item(i, 1)
            if item_site and item_passwo:
              site = item_site.text()
              passwo = item_passwo.text()
              data[site] = passwo
        with open("passwords.json", "w", encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=6)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())