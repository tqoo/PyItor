from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QFileDialog, QMenuBar
from PyQt5.QtGui import QIcon
import keyboard as kb
from json import loads
xfile = None
content = None
filetopngraw = open('filetopng.json', 'r')
filetopng = loads(filetopngraw.read())

def xopen():
    global xfile
    global content
    filex = ''
    xfile = QFileDialog().getOpenFileName()[0]
    content = xfile
    long_filename = xfile.split('.')
    filex = long_filename[1]
    with open(xfile, 'r+') as xfile:
        xfile = xfile.read()
    icon = QIcon('icons/' + filetopng[filex])
    app.setWindowIcon(icon)
    text.setText(xfile)

def save(xxfile):
    with open(xxfile, 'w') as xfile:
        xfile = xfile.write(text.toPlainText())
app = QApplication([])
text = QTextEdit()
text.show()
print(content, xfile)
xopen()
kb.add_hotkey('ctrl+s', lambda: save(content))
kb.add_hotkey('ctrl+o', lambda: xopen())
app.exec_()