# Calculate the first pile of gold coins
Pile_1 = (15 * 8) + 20

# Calculate the second pile of gold coins
Pile_2 = Pile_1 - (5**2) + 30

# Calculate the third pile of gold coins
Pile_3 = (Pile_1 + Pile_2) / 2 + 100

# Calculate the hidden treasure pile
Hidden_Treasure = (Pile_1 + Pile_2 + Pile_3) * 1.25

total = Pile_1 + Pile_2 + Pile_3 + Hidden_Treasure

# Print the results
print("Coins:", total)