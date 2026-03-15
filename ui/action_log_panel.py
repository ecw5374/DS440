from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit


class ActionLogPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Action Log"))
        layout.addWidget(self.log_box)
        self.setLayout(layout)

    def render_log(self, action_log):
        self.log_box.setPlainText("\n".join(action_log))