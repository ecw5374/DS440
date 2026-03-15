from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.new_hand_btn = QPushButton("New Hand")
        self.next_step_btn = QPushButton("Next Step")
        self.run_to_end_btn = QPushButton("Run To End")

        layout = QHBoxLayout()
        layout.addWidget(self.new_hand_btn)
        layout.addWidget(self.next_step_btn)
        layout.addWidget(self.run_to_end_btn)

        self.setLayout(layout)