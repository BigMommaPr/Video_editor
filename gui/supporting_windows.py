from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QDialogButtonBox, \
    QVBoxLayout, QLabel, QHBoxLayout
import sys


class TrimDialogWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("trim dialog")
        self.setMinimumWidth(250)

        main_text = self._get_text_label(
            "Select the fragment that will remain:"
        )
        start_text = self._get_text_label("start time")
        end_text = self._get_text_label("end time")

        self._set_up_time_edit_widgets()
        choice_button = self._get_choice_button()

        self._set_up_layouts(choice_button, end_text, main_text, start_text)

    def _get_text_label(self, text):
        label = QtWidgets.QLabel(self)
        label.setText(text)
        label.adjustSize()

        return label

    def _set_up_time_edit_widgets(self):
        self.start_edit = QtWidgets.QTimeEdit(self)
        self.start_edit.setDisplayFormat("mm:ss")

        self.end_edit = QtWidgets.QTimeEdit(self)
        self.end_edit.setDisplayFormat("mm:ss")

    def _get_choice_button(self):
        choice_button = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        choice_button.accepted.connect(self.accept)
        choice_button.rejected.connect(self.reject)

        return choice_button

    def _set_up_layouts(self, choice_button, end_text, main_text, start_text):
        start_layout = QHBoxLayout()
        start_layout.addWidget(start_text)
        start_layout.addWidget(self.start_edit)

        end_layout = QHBoxLayout()
        end_layout.addWidget(end_text)
        end_layout.addWidget(self.end_edit)

        main_layout = QVBoxLayout()
        main_layout.addWidget(main_text)
        main_layout.addLayout(start_layout)
        main_layout.addLayout(end_layout)
        main_layout.addWidget(choice_button)

        self.setLayout(main_layout)

    def get_fragment_time(self) -> list:
        print(self.start_edit.time().second())
        return [self.start_edit.time(), self.end_edit.time()]


def run_trim_dialog_window() -> list:
    window = TrimDialogWindow()
    window.show()
    if window.exec() == QDialog.DialogCode.Accepted:
        return window.get_fragment_time()
    else:
        return None
