import json
import csv
import sys
from PyQt5 import QtWidgets
from GUI import Ui_Form


class db():

    def __init__(self, name):
        self.name = name
        self.keydict = {}
        self.searchdict = {}
        self.checkChanges = True
        self.saved = False

    def insert(self, key='', value=None):
        self.saved = False
        if value is None:
            value = []
        if not key:
            key = ui.lineEdit_4.text()
            value = [ui.lineEdit_5.text(), ui.lineEdit_6.text(), ui.lineEdit_7.text()]
            if not key:
                return
        self.insertDB(key, value)
        self.printData()
        self.checkChanges = True

    def insertDB(self, key='', value=[]):
        if key in self.keydict:
            print('Duplicate record')
            return
        else:
            self.keydict[key] = value
        if value[0] in self.searchdict:
            self.searchdict[value[0]].append(key)
        else:
            self.searchdict[value[0]] = [key]

    def deleteRec(self, key='', value=''):
        self.saved = False
        if not value and not key:
            try:
                value = ui.lineEdit_3.text()
                key = self.searchdict[value][0]
            except Exception:
                return
        else:
            value = self.keydict[key][0]
        self.deleteFromDB(key, value)
        self.printData()

    def deleteFromDB(self, key='', value=''):
        self.searchdict[value].remove(key)
        self.keydict.pop(key)

    def editRecord(self, key, value):
        self.deleteRec(key=key)
        self.insertDB(key, value)

    def save(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QWidget(), "Save", "", "JSON (*.json*)",
                                                         options=QtWidgets.QFileDialog.Options())
        if fileName:
            try:
                print("saving", fileName)
                data = list()
                data.append(self.keydict)
                data.append(self.searchdict)
                with open(fileName[0], 'w') as f:
                    f.write(json.dumps(data))
                self.saved = True
            except Exception:
                pass

    def open(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(), "Open", "", "JSON (*.json*)",
                                                         options=QtWidgets.QFileDialog.Options())
        if fileName:
            try:
                print('open')
                with open(fileName[0], 'r') as f:
                    data = json.load(f)
                self.keydict = data[0]
                self.searchdict = data[1]
                self.printData()
                self.saved = True
            except Exception:
                pass

    def exportToScv(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QWidget(), "Export to CSV", "", "CSV (*.csv*)",
                                                         options=QtWidgets.QFileDialog.Options())
        if fileName:
            try:
                with open(fileName[0], 'w', newline='') as f:
                    w = csv.writer(f)
                    for i in self.keydict:
                        w.writerow((i, self.keydict[i][0], self.keydict[i][1], self.keydict[i][2]))
            except Exception:
                pass

    def importFromScv(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(), "Import CSV", "", "CSV (*.csv*)",
                                                         options=QtWidgets.QFileDialog.Options())
        if fileName:
            try:
                self.keydict.clear()
                self.searchdict.clear()
                with open(fileName[0], 'r') as f:
                    for data in csv.reader(f):
                        self.insert(data[0], [data[1], data[2], data[3]])
            except Exception:
                pass

    def updateData(self, item):
        try:
            if self.checkChanges:
                print(ui.tableWidget.item(item.row(), item.column() - 1).text())
                phone = ui.tableWidget.item(item.row(), 0).text()
                name = ui.tableWidget.item(item.row(), 1).text()
                birth = ui.tableWidget.item(item.row(), 2).text()
                address = ui.tableWidget.item(item.row(), 3).text()
                self.editRecord(phone, [name, birth, address])
                self.printData()
        except Exception:
            self.printData()
            pass

    def printData(self):
        ui.tableWidget.setRowCount(len(self.keydict))
        self.checkChanges = False
        j = 0
        for i in self.keydict:
            print(i, self.keydict[i][0], self.keydict[i][1], self.keydict[i][2])
            ui.tableWidget.setItem(j, 0, QtWidgets.QTableWidgetItem(i))
            ui.tableWidget.setItem(j, 1, QtWidgets.QTableWidgetItem(self.keydict[i][0]))
            ui.tableWidget.setItem(j, 2, QtWidgets.QTableWidgetItem(str(self.keydict[i][1])))
            ui.tableWidget.setItem(j, 3, QtWidgets.QTableWidgetItem(self.keydict[i][2]))
            j += 1
        self.checkChanges = True

    def test(self):
        self.insert('+78005553535', ['Ivanov Ivan Ivanovich', 18, 'Lenina street'])
        self.insert('+78005553635', ['DDDvanov Ivan Ivanovich', 17, 'Lenina street'])
        self.insert('+78005553735', ['DDDvanov Ivan Ivanovich', 16, 'Lenina street'])
        self.insert('+78005553835', ['DDDvanov Ivan Ivanovich', 15, 'Lenina street'])
        self.insert('+78005553935', ['DDDvanov Ivan Ivanovich', 14, 'Lenina street'])
        self.insert('+78005553135', ['DDDvanov Ivan Ivanovich', 13, 'Lenina street'])
        self.insert('+78005553235', ['DDDvanov Ivan Ivanovich', 12, 'Lenina street'])
        self.insert('+78005553335', ['DDDvanov Ivan Ivanovich', 11, 'Lenina street'])
        self.insert('+78005553435', ['DDDvanov Ivan Ivanovich', 10, 'Lenina street'])
        self.insert('+78005553531', ['DDDvanov Ivan Ivanovich', 27, 'Lenina street'])
        self.insert('+78005553832', ['DDDvanov Ivan Ivanovich', 27, 'Lenina street'])

    def searchData(self):
        try:
            value = ui.lineEdit_3.text()
            key = self.searchdict[value][0]
        except Exception:
            return
        l1 = self.searchdict[value]
        data = [str(i) + ' ' + str(self.keydict[i][0]) + ' ' + str(self.keydict[i][1]) + ' ' + str(self.keydict[i][2]) for i in l1]
        QtWidgets.QMessageBox.question(QtWidgets.QWidget(), ' Нашёл!', '\n'.join(data), QtWidgets.QMessageBox.Ok)


class MainWindow(QtWidgets.QWidget):

    def closeEvent(self, event):
        if not phonebook.saved:
            reply = QtWidgets.QMessageBox.question(self, 'Window Close', 'Do u want to save?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                phonebook.save()

            event.accept()
            print('Window closed')


if __name__ == "__main__":
    # Create application
    app = QtWidgets.QApplication(sys.argv)
    # Create form and init UI
    #Form = QtWidgets.QWidget()
    Form = MainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    # Hook logic
    phonebook = db('test')
    phonebook.printData()
    phonebook.test()
    phonebook.printData()
    ui.pushButton.clicked.connect(phonebook.searchData)
    ui.pushButton_4.clicked.connect(phonebook.save)
    ui.pushButton_3.clicked.connect(Form.close)
    ui.pushButtonO.clicked.connect(phonebook.open)
    ui.pushButtonE.clicked.connect(phonebook.exportToScv)
    ui.pushButtonI.clicked.connect(phonebook.importFromScv)
    ui.pushButton_5.clicked.connect(phonebook.insert)
    ui.pushButton_2.clicked.connect(phonebook.deleteRec)
    ui.tableWidget.itemChanged.connect(phonebook.updateData)

    # Run main loop
    sys.exit(app.exec_())
