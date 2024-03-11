from PyQt6 import QtWidgets
# from PyQt6 import QtString
from PyQt6 import uic
from calc_ui import Ui_Form
 
import sys

class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_0.clicked.connect(lambda: self.push_symbol('0'))
        self.ui.pushButton_1.clicked.connect(lambda: self.push_symbol('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.push_symbol('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.push_symbol('3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.push_symbol('4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.push_symbol('5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.push_symbol('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.push_symbol('7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.push_symbol('8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.push_symbol('9'))
        self.ui.pushButton_dot.clicked.connect(lambda: self.push_symbol('.'))
        self.ui.pushButton_minus.clicked.connect(lambda: self.push_symbol('-'))
        self.ui.pushButton_plus.clicked.connect(lambda: self.push_symbol('+'))
        self.ui.pushButton_multiply.clicked.connect(lambda: self.push_symbol('*'))
        self.ui.pushButton_devide.clicked.connect(lambda: self.push_symbol('/'))
        self.ui.pushButton_mod.clicked.connect(lambda: self.push_symbol('%'))
        self.ui.pushButton_pow.clicked.connect(lambda: self.push_symbol('^'))
        self.ui.pushButton_opening_bracet.clicked.connect(lambda: self.push_symbol('('))
        self.ui.pushButton_closing_bracket.clicked.connect(lambda: self.push_symbol(')'))
        self.ui.pushButton_delete.clicked.connect(lambda: self.del_expression())
        self.ui.pushButton_clear.clicked.connect(lambda: self.clear_expression())
        self.ui.pushButton_calculate.clicked.connect(lambda: self.calculate_expression())
        
    def calculate_expression(self) -> None:
        text = self.ui.lineEdit_result.text()
        self.ui.lineEdit_expression.setText(text)
        pass


    def clear_expression(self) -> None:
        self.ui.lineEdit_expression.setText("")
        self.ui.lineEdit_result.setText("")
        pass

    def del_expression(self) -> None:
        text = self.ui.lineEdit_expression.text()
        text = text[:-1]
        self.ui.lineEdit_expression.setText(text)
        self.update_precalc()
        pass
        
    
    def update_precalc(self) -> None:
        text = self.ui.lineEdit_expression.text().replace("^", "**")
        try:
            result = eval(text)
            self.ui.lineEdit_result.setText(str(result))
        except:
            self.ui.lineEdit_result.setText("")
        pass

    def push_symbol(self, symbol) -> None:
        text = self.ui.lineEdit_expression.text()
        text = self.push_symbol_properly(text, symbol)
        self.ui.lineEdit_expression.setText(text)
        self.update_precalc()
        pass

    def push_symbol_properly(self, string: str, symbol) -> str:
        if((symbol in ('*' ,'/' , '^' , '%', ')')) and len(string) > 0 and (string[len(string) - 1] not in ('+' , '-' , '/' , '*' , '%' , '^' , '('))):
            string += symbol
        if ((symbol in ('+', '-')) and ((len(string) == 0) or (string[len(string) - 1] not in ('+' , '-' , '/' , '*' , '%' , '^')))):
            string += symbol
        if (symbol == '.' and len(string) > 0 and ('0' <= string[len(string) - 1] <= '9')):
            string += symbol
        if('0' <= symbol <= '9'):
            if(len(string) == 0):
                string += symbol
            else:
                i = len(string) - 1
                while i >= 0 and '0' <= string[i] <= '9':
                    i -= 1
                if(string[i] == '.'):
                    string += symbol
                elif (i == len(string) - 1 or (string[i + 1] != '0') ):
                    if (i < 0):
                        string += symbol
                    elif(string[i] in ('+' , '-' , '/' , '*' , '%' , '^' , '(')):
                        string += symbol
        if( symbol == '('):
            if(len(string) == 0):
                string += symbol
            elif(string[len(string) - 1] in ('+' , '-' , '/' , '*' , '%' , '^', '(')):
                string += symbol
        return string



app = QtWidgets.QApplication(sys.argv)

window = AppMainWindow()
window.show()

app.exec()
