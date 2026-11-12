from PySide6.QtWidgets import QFrame, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent


class DropAwareFrame(QFrame):
    def __init__(self, parent=None, on_files_dropped=None):
        super().__init__(parent)
        self.on_files_dropped = on_files_dropped
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        mime = event.mimeData()
        if mime.hasUrls():
            for url in mime.urls():
                if url.isLocalFile():
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dragMoveEvent(self, event: QDragEnterEvent):
        mime = event.mimeData()
        if mime.hasUrls():
            for url in mime.urls():
                if url.isLocalFile():
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event: QDropEvent):
        mime = event.mimeData()
        if not mime.hasUrls():
            event.ignore()
            return

        file_paths = [url.toLocalFile() for url in mime.urls() if url.isLocalFile()]

        if not file_paths:
            event.ignore()
            return

        if len(file_paths) > 1:
            QMessageBox.warning(
                self,
                "Multiple files dropped",
                "Please drop only one image at a time."
            )
            event.ignore()
            return

        single_path = file_paths[0]

        if self.on_files_dropped:
            self.on_files_dropped(single_path)

        event.acceptProposedAction()
