def order_sandwich(*ingredients):
    """Print a summary of the sandwich being ordered."""
    if ingredients:
        print("\nYou have ordered a sandwich with the following ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
    else:
        print("\nYou have ordered a plain sandwich with no additional ingredients.")

order_sandwich("turkey", "pesto", "lettuce", "tomato", "cucumber")
order_sandwich("ham", "cheese", "pickled onions")