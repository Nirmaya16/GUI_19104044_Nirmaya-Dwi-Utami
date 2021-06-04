from PyQt5.QtWidgets import *

app = QApplication([])

#kelas QPushButton
#menampilkan tombol click di dalam form 
button = QPushButton('Click')

def on_button_clicked():
    #kelas QMessageBox
    alert = QMessageBox()
    
    #kelas QLabel
    #setText: Memasukkan teks ke dalam objek label
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)

button.show()
app.exec_();