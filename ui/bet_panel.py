from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QDoubleSpinBox,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QMessageBox
)


class BetPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.contract_label = QLabel("Select Open Contract")
        self.contract_combo = QComboBox()

        self.stake_label = QLabel("Stake Amount")
        self.stake_input = QDoubleSpinBox()
        self.stake_input.setMinimum(1.0)
        self.stake_input.setMaximum(1000000.0)
        self.stake_input.setDecimals(2)
        self.stake_input.setValue(10.0)

        self.place_bet_btn = QPushButton("Place Bet")

        self.open_bets_label = QLabel("Open Bets")
        self.open_bets_list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.contract_label)
        layout.addWidget(self.contract_combo)
        layout.addWidget(self.stake_label)
        layout.addWidget(self.stake_input)
        layout.addWidget(self.place_bet_btn)
        layout.addWidget(self.open_bets_label)
        layout.addWidget(self.open_bets_list)
        self.setLayout(layout)

        self._contracts = []

    def set_contracts(self, contracts):
        current_id = self.current_contract_id()

        self._contracts = [c for c in contracts if c.is_open and not c.resolved]
        self.contract_combo.clear()

        for c in self._contracts:
            label = f"{c.description} | price={c.price:.3f}"
            self.contract_combo.addItem(label, c.contract_id)

        if current_id is not None:
            idx = self.contract_combo.findData(current_id)
            if idx >= 0:
                self.contract_combo.setCurrentIndex(idx)

        has_open = len(self._contracts) > 0
        self.contract_combo.setEnabled(has_open)
        self.stake_input.setEnabled(has_open)
        self.place_bet_btn.setEnabled(has_open)

    def current_contract_id(self):
        return self.contract_combo.currentData()

    def render_open_bets(self, bettor):
        self.open_bets_list.clear()
        for bet in bettor.open_bets:
            text = (
                f"{bet.contract_id} | "
                f"stake={bet.stake:.2f} | "
                f"price={bet.price:.3f} | "
                f"shares={bet.shares:.3f}"
            )
            self.open_bets_list.addItem(QListWidgetItem(text))

    def show_error(self, message: str):
        QMessageBox.warning(self, "Bet Error", message)

    def show_info(self, message: str):
        QMessageBox.information(self, "Bet Placed", message)