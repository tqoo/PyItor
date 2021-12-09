#https://github.com/microsoft/vscode-icons/#tree/main/icons/light
from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QFileDialog, QMenuBar, QShortcut, QVBoxLayout, QWidget, QAction
from PyQt5.QtGui import QIcon, QKeySequence
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
    print('got open file name')
    content = xfile
    long_filename = xfile.split('.')
    filex = long_filename[1]
    with open(xfile, 'r+') as xfile:
        try:
            xfile = xfile.read()
        except UnicodeDecodeError:
            print("Welp, that can't be read.")
            quit()
    try:
        icon = QIcon('icons/' + filetopng[filex])
    except KeyError:
        icon = QIcon('icons/default.png')
    app.setWindowIcon(icon)
    print('setting text')
    text.setText(xfile)

def save(xxfile):
    with open(xxfile, 'w+') as xfile:
        xfile = xfile.write(text.toPlainText())
#Initiate Widgets
app = QApplication([])
layout = QVBoxLayout()
menu = QMenuBar()
text = QTextEdit()
window = QWidget()
qopen = QAction('&Open')
qsave = QAction('&Save')
fileMenu = menu.addMenu('&File')

qopen.triggered.connect(xopen)  
qsave.triggered.connect(lambda: save(content))
fileMenu.addAction(qopen)
fileMenu.addAction(qsave)
layout.addWidget(menu)
layout.addWidget(text)
text.show()
window.setLayout(layout)
window.show()
print(content, xfile)
xopen()
app.exec_()