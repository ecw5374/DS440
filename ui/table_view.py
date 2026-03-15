from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QFrame
)
from PyQt5.QtCore import Qt


class TableView(QWidget):
    def __init__(self):
        super().__init__()

        self.street_label = QLabel("Street: --")
        self.pot_label = QLabel("Pot: 0")
        self.board_label = QLabel("Board: --")

        self.player_labels = []

        layout = QVBoxLayout()
        layout.addWidget(self.street_label)
        layout.addWidget(self.pot_label)
        layout.addWidget(self.board_label)

        grid = QGridLayout()

        for i in range(4):
            box = QFrame()
            box.setFrameShape(QFrame.Box)

            box_layout = QVBoxLayout()

            label = QLabel(f"Player {i + 1}")
            label.setAlignment(Qt.AlignCenter)
            label.setWordWrap(True)

            box_layout.addWidget(label)
            box.setLayout(box_layout)

            self.player_labels.append(label)

            row = 0 if i < 2 else 1
            col = i % 2
            grid.addWidget(box, row, col)

        layout.addLayout(grid)
        self.setLayout(layout)

    def render_state(self, state):
        if state is None:
            self.street_label.setText("Street: --")
            self.pot_label.setText("Pot: 0")
            self.board_label.setText("Board: --")
            for i, label in enumerate(self.player_labels):
                label.setText(f"Player {i + 1}")
            return

        self.street_label.setText(f"Street: {state.street.upper()}")
        self.pot_label.setText(f"Pot: {state.pot}")

        board_text = " ".join(str(c) for c in state.community_cards) if state.community_cards else "--"
        self.board_label.setText(f"Board: {board_text}")

        for i, player in enumerate(state.players):
            status = []
            if player.folded:
                status.append("FOLDED")
            if player.all_in:
                status.append("ALL-IN")

            status_text = " | ".join(status) if status else "ACTIVE"

            text = (
                f"{player.name}\n"
                f"Stack: {player.stack}\n"
                f"Bet: {player.current_bet}\n"
                f"Status: {status_text}"
            )
            self.player_labels[i].setText(text)