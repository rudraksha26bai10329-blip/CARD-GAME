# Problem Statement & Technical Specification

## Objective
Design and implement an extensible, object-oriented text-based card game engine in Python capable of running round-based card games for multiple players.

## Requirements
1. **Card Modeling**: Represent individual cards with rank (`2-10, J, Q, K, A`), suit (`♠, ♥, ♦, ♣`), and comparable numerical values.
2. **Deck Operations**: Construct a standard 52-card deck, support random shuffling, and implement safe card drawing with edge-case handling.
3. **Player State**: Maintain individual player identity, current hand state, and cumulative score.
4. **Game Controller**: Implement a controller managing game loops, round-based card distribution, round outcome evaluations (including ties), and overall winner determinations.
5. **Quality Assurance**: Cover core business logic with unit tests verifying deck limits, rank comparison, and score accumulation.
