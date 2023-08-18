import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QClipboard
from googletrans import Translator

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('自動翻譯程式')
        
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.check_clipboard)

        self.text_label = QLabel('框選的文字將自動翻譯成中文:')
        self.translation_label = QLabel('翻譯結果將在這裡顯示')

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.addWidget(self.text_label)
        layout.addWidget(self.translation_label)

        self.setLayout(layout)

    def check_clipboard(self):
        mime_data = self.clipboard.mimeData()
        print("Ctrl + C",flush=True)
        if mime_data.hasText():
            selected_text = mime_data.text()
            translator = Translator()
            translation = translator.translate(selected_text, src='auto', dest='zh-CN')
            self.translation_label.setText('翻譯結果: ' + translation.text)
        else:
            self.translation_label.setText('翻譯結果將在這裡顯示')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec())
