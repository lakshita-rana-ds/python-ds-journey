# ================
# DAY 17 - Statistics - Probability Basics: Events, Rules
# DATE - 25 July, 2026
# STATUS - Done
# ================

import numpy as np
import random
from itertools import product

# Step 1: Sample space and event
sample_space = [1, 2, 3, 4, 5, 6]
print("Sample Space:", sample_space)

event_even = [x for x in sample_space if x % 2 == 0]
print("Event (even numbers):", event_even)

probability_even = len(event_even) / len(sample_space)
print("Probability of rolling even:", probability_even)

# Step 2: Simulating probability (Law of Large Numbers)
rolls = [random.randint(1, 6) for _ in range(10000)]
even_count = sum(1 for roll in rolls if roll % 2 == 0)

simulated_probability = even_count / len(rolls)
print("Simulated probability of even (10,000 rolls):", simulated_probability)

# Step 3: Addition Rule - P(A or B)
event_A = set(x for x in sample_space if x % 2 == 0)
event_B = set(x for x in sample_space if x > 4)

prob_A = len(event_A) / len(sample_space)
prob_B = len(event_B) / len(sample_space)
prob_A_and_B = len(event_A & event_B) / len(sample_space)

prob_A_or_B = prob_A + prob_B - prob_A_and_B
print("P(A):", prob_A)
print("P(B):", prob_B)
print("P(A and B):", prob_A_and_B)
print("P(A or B):", prob_A_or_B)

# Step 4: Multiplication Rule - independent events
prob_heads = 0.5
prob_six = 1/6

prob_heads_and_six = prob_heads * prob_six
print("P(Heads and rolling a 6):", prob_heads_and_six)

# Step 5: Complement Rule
prob_not_even = 1 - prob_A
print("P(not even):", prob_not_even)

# ================================
# DAY 17 TASK
# ================================

# Using a standard deck of 52 cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
print("\nTotal cards in deck:", len(deck))

# 1. Sample space and event: probability of drawing a King
kings = [card for card in deck if card.startswith("K")]
prob_king = len(kings) / len(deck)
print("Theoretical probability of drawing a King:", prob_king)

# 2. Simulate drawing a card 5000+ times (with replacement) and check King frequency
draws = [random.choice(deck) for _ in range(5000)]
king_draws = sum(1 for card in draws if card.startswith("K"))
simulated_prob_king = king_draws / len(draws)
print("Simulated probability of drawing a King (5000 draws):", simulated_prob_king)

# 3. Addition Rule - P(King or Heart)
event_king = set(card for card in deck if card.startswith("K"))
event_heart = set(card for card in deck if "Hearts" in card)

prob_event_king = len(event_king) / len(deck)
prob_event_heart = len(event_heart) / len(deck)
prob_king_and_heart = len(event_king & event_heart) / len(deck)

prob_king_or_heart = prob_event_king + prob_event_heart - prob_king_and_heart
print("\nP(King):", prob_event_king)
print("P(Heart):", prob_event_heart)
print("P(King and Heart):", prob_king_and_heart)
print("P(King or Heart):", prob_king_or_heart)

# 4. Multiplication Rule - independent events (drawing with replacement)
# P(King on first draw AND Queen on second draw, with replacement so independent)
prob_king_draw1 = len(kings) / len(deck)
queens = [card for card in deck if card.startswith("Q")]
prob_queen_draw2 = len(queens) / len(deck)

prob_king_then_queen = prob_king_draw1 * prob_queen_draw2
print("\nP(King then Queen, with replacement):", prob_king_then_queen)




