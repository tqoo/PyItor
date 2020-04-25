from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon
import keyboard as kb
def xopen():
    global xfile
    global content
    filex = ''
    filetype = {
        'py' : 'python.png',
        'md' : 'markdown.png'
    }
    xfile = QFileDialog().getOpenFileName()[0]
    content = xfile
    long_filename = xfile.split('.')
    filex = long_filename[1]
    with open(xfile, 'r+') as xfile:
        xfile = xfile.read()
    icon = QIcon('icons/' + filetype[filex])
    app.setWindowIcon(icon)

def save(xxfile):
    with open(xxfile, 'w') as xfile:
        xfile = xfile.write(text.toPlainText())
app = QApplication([])
xopen()
text = QTextEdit()
text.setText(xfile)
text.show()
print(content, xfile)
#print('TextBox done')
kb.add_hotkey('ctrl+s', lambda: save(content))
app.exec_()