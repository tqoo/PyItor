from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QFileDialog
xfile = '''
Lorem ipsum blah blah blah
This that this that
oof oof oof
'''
app = QApplication([])
#print('Initilise App')
xfile = QFileDialog().getOpenFileName()
with open(xfile[0], 'r+') as xfile:
    xfile = xfile.read()
text = QTextEdit()
text.setText(xfile)
text.show()
#print('TextBox done')
app.exec_()