import random

def recommend_food():
    # Define food options for each continent
    continents = {
        'Asia': ['Curry', 'Sushi', 'Noodles'],
        'Europe': ['Pizza', 'Pasta', 'Croissant'],
        'Africa': ['Tagine', 'Jollof Rice', 'Bunny Chow'],
        'North America': ['Burger', 'Tacos', 'Poutine'],
        'South America': ['Empanadas', 'Ceviche', 'Feijoada'],
        'Australia': ['Pavlova', 'Meat Pie', 'Lamington']
    }

    # Generate random continent and spice preference
    continent = random.choice(list(continents.keys()))
    is_spicy = random.choice([True, False])

    # Filter food based on spice preference
    recommended_food = continents[continent]
    if not is_spicy:
        recommended_food = [food for food in recommended_food if 'spicy' not in food.lower()]

    # Display recommendation
    print(f"You should try {random.choice(recommended_food)} from {continent} continent.")

# Example usage
recommend_food()
