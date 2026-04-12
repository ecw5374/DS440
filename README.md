# Poker Prediction Market

A Python desktop application that simulates a 4-player poker game with a spectator-facing prediction market. Spectators can place bets on public-information contracts such as who will win the hand or whether the hand reaches showdown.

## Features

- 4 simulated poker players
- Step-by-step poker hand progression
- Prediction market contracts
- Spectator betting interface
- Bankroll tracking
- Multi-hand session support
- PyQt5 desktop UI

## Betting Assistant

The desktop app now includes a state-aware Assistant tab. It can answer:
- current table state questions such as pot, street, board, active players, and bankroll
- public-information card probability questions such as whether a specific card can appear on the board
- recommendation questions such as the best bets available right now

The assistant is deterministic and only uses public game state while a hand is live.
