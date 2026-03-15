from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
)


class MarketPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.bankroll_label = QLabel("Spectator Bankroll: 1000.00")
        self.contract_list = QListWidget()
        self.settled_bets_label = QLabel("Settled Bets")
        self.settled_bets_list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Prediction Market"))
        layout.addWidget(self.bankroll_label)
        layout.addWidget(self.contract_list)
        layout.addWidget(self.settled_bets_label)
        layout.addWidget(self.settled_bets_list)
        self.setLayout(layout)

    def render_contracts(self, contracts):
        self.contract_list.clear()

        for c in contracts:
            status = c.status_text()
            outcome_text = ""
            if c.resolved:
                outcome_text = f" | outcome={c.outcome}"

            text = (
                f"{c.contract_id} | "
                f"{c.description} | "
                f"price={c.price:.3f} | "
                f"{status}"
                f"{outcome_text}"
            )
            self.contract_list.addItem(QListWidgetItem(text))

    def render_bankroll(self, bettor):
        self.bankroll_label.setText(f"Spectator Bankroll: {bettor.bankroll:.2f}")

    def render_settled_bets(self, bettor):
        self.settled_bets_list.clear()
        for bet in bettor.settled_bets:
            result = "WIN" if bet.won else "LOSS"
            text = (
                f"{bet.contract_id} | {result} | "
                f"stake={bet.stake:.2f} | payout={bet.payout:.2f}"
            )
            self.settled_bets_list.addItem(QListWidgetItem(text))