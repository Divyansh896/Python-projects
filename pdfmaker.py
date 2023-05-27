from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QFileDialog
from untitled import Ui_Dialog
import sys
import datetime
from PIL import Image
from PyPDF2 import PdfMerger
merger = PdfMerger()
file =[]
class appwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.browse)
        self.ui.pushButton_2.clicked.connect(self.merge)
        self.ui.pushButton_3.clicked.connect(self.makepdf)
        self.show()

    def browse(self):
        global file_directory
        file_directory,_ = QFileDialog.getOpenFileNames(self,'open file','F:\\','All Files(*);;PNG Files(*.png);;Jpg Files(*.jpg);;PDF Files(*.pdf)') #to select file
        # print(type(file_directory))
        for pdf in file_directory:
            print(pdf)
            self.ui.listWidget.addItem(pdf)


    def merge(self):
        for pdf in file_directory:
            merger.append(pdf, 'rb')
        merger.write('merged file.pdf')
        merger.close()

    def makepdf(self):
        # fname = QFileDialog.getSaveFileName(self,'save file')
        for pdf in file_directory:
            if pdf.endswith('.jpg') or pdf.endswith('.png'):
                i  = Image.open(pdf)
                i = i.convert('RGB')
                file.append(i)
        file.pop()
        dt = datetime.datetime.now().date()
        i.save(f'{dt}.pdf',save_all = True,append_images = file),filter('PDF Files(*.pdf)')



if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = appwindow()

        sys.exit(app.exec_())
