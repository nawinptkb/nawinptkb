# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pyqt_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(603, 402)
        Dialog.setStyleSheet("#Form{\n"
"    background:#202020;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background:#d2d3d7;\n"
"    border:none;\n"
"    font-family: Arial, Helvetica, sans-serif;\n"
"    font-size:20px;\n"
"    color:#202020;\n"
"}")
        self.seven = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("7"))
        self.seven.setGeometry(QtCore.QRect(40, 180, 113, 32))
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("8"))
        self.eight.setGeometry(QtCore.QRect(180, 180, 113, 32))
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("9"))
        self.nine.setGeometry(QtCore.QRect(320, 180, 113, 32))
        self.nine.setObjectName("nine")
        self.four = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("4"))
        self.four.setGeometry(QtCore.QRect(40, 230, 113, 32))
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("5"))
        self.five.setGeometry(QtCore.QRect(180, 230, 113, 32))
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("6"))
        self.six.setGeometry(QtCore.QRect(320, 230, 113, 32))
        self.six.setObjectName("six")
        self.one = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("1"))
        self.one.setGeometry(QtCore.QRect(40, 280, 113, 32))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("2"))
        self.two.setGeometry(QtCore.QRect(180, 280, 113, 32))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("3"))
        self.three.setGeometry(QtCore.QRect(320, 280, 113, 32))
        self.three.setObjectName("three")
        self.Add = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("+"))
        self.Add.setGeometry(QtCore.QRect(450, 280, 113, 32))
        self.Add.setObjectName("Add")
        self.Result = QtWidgets.QPushButton(Dialog, clicked = lambda:self.result())
        self.Result.setGeometry(QtCore.QRect(450, 340, 113, 32))
        self.Result.setObjectName("Result")
        self.Subtract = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("-"))
        self.Subtract.setGeometry(QtCore.QRect(450, 230, 113, 32))
        self.Subtract.setObjectName("Subtract")
        self.Multiply = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("*"))
        self.Multiply.setGeometry(QtCore.QRect(450, 180, 113, 32))
        self.Multiply.setObjectName("Multiply")
        self.Divide = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("/"))
        self.Divide.setGeometry(QtCore.QRect(450, 130, 113, 32))
        self.Divide.setObjectName("Divide")
        self.Clear_input = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("C"))
        self.Clear_input.setGeometry(QtCore.QRect(320, 130, 113, 32))
        self.Clear_input.setObjectName("Clear_input")
        self.delete_entry = QtWidgets.QPushButton(Dialog, clicked = lambda:self.remove_it())
        self.delete_entry.setGeometry(QtCore.QRect(180, 130, 113, 32))
        self.delete_entry.setObjectName("delete_entry")
        self.Power2 = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("**"))
        self.Power2.setGeometry(QtCore.QRect(40, 130, 113, 32))
        self.Power2.setObjectName("Power2")
        self.zero = QtWidgets.QPushButton(Dialog, clicked = lambda:self.press_it("0"))
        self.zero.setGeometry(QtCore.QRect(40, 330, 113, 32))
        self.zero.setObjectName("zero")
        self.Period = QtWidgets.QPushButton(Dialog, clicked = lambda:self.dot_it())
        self.Period.setGeometry(QtCore.QRect(180, 330, 113, 32))
        self.Period.setObjectName("Period")
        self.OutputLabel = QtWidgets.QLabel(Dialog)
        self.OutputLabel.setGeometry(QtCore.QRect(50, 30, 501, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.OutputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OutputLabel.setLineWidth(2)
        self.OutputLabel.setMidLineWidth(1)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OutputLabel.setObjectName("OutputLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

#Remove character
    def remove_it(self):
        #Grab what's on the screen already
        screen = self.OutputLabel.text()
        #Remove last item in list
        screen = screen[:-1]
        #Output back to the screen
        self.OutputLabel.setText(screen)

    #Add Decimal
    def dot_it(self):
        screen = self.OutputLabel.text()

        if screen[-1] == ".":
            pass
        else:
            self.OutputLabel.setText(f'{screen}.')

    #Pressing buttons algorithm
    def press_it(self,pressed):
        if pressed == "C":
            self.OutputLabel.setText("0")

        else:
            #Check to see if starts with 0 and delete 0
            if self.OutputLabel.text() == "0":
                self.OutputLabel.setText("")
            #Concatenate the pressed button with what was there already
            self.OutputLabel.setText(f'{self.OutputLabel.text()}{pressed}')

    #Result Button
    def result(self):
        screen = self.OutputLabel.text()
        try:
            #Do the math
            answer = eval(screen)
            #Output answer to the screen
            self.OutputLabel.setText(str(answer))

        except ZeroDivisionError:
            #Output error to the screen
            self.OutputLabel.setText(str("Can't Divide with Zero"))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.seven.setText(_translate("Dialog", "7"))
        self.eight.setText(_translate("Dialog", "8"))
        self.nine.setText(_translate("Dialog", "9"))
        self.four.setText(_translate("Dialog", "4"))
        self.five.setText(_translate("Dialog", "5"))
        self.six.setText(_translate("Dialog", "6"))
        self.one.setText(_translate("Dialog", "1"))
        self.two.setText(_translate("Dialog", "2"))
        self.three.setText(_translate("Dialog", "3"))
        self.Add.setText(_translate("Dialog", "+"))
        self.Result.setText(_translate("Dialog", "="))
        self.Subtract.setText(_translate("Dialog", "-"))
        self.Multiply.setText(_translate("Dialog", "*"))
        self.Divide.setText(_translate("Dialog", "/"))
        self.Clear_input.setText(_translate("Dialog", "C"))
        self.delete_entry.setText(_translate("Dialog", "Del"))
        self.Power2.setText(_translate("Dialog", "Expo"))
        self.zero.setText(_translate("Dialog", "0"))
        self.Period.setText(_translate("Dialog", "."))
        self.OutputLabel.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
