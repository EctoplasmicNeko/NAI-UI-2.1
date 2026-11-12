from PySide6.QtWidgets import QProgressBar
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QRect

class VerticalTextProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOrientation(Qt.Vertical)
        self.setTextVisible(True)

    def paintEvent(self, event):
        original_text_visible = self.isTextVisible()
        self.setTextVisible(False)
        super().paintEvent(event)
        self.setTextVisible(original_text_visible)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        text = self.text() or f"{self.value()}%"

        painter.translate(0, self.height())
        painter.rotate(-90)

        text_rect = QRect(0, 0, self.height(), self.width())
        painter.drawText(text_rect, Qt.AlignCenter, text)

        painter.end()
