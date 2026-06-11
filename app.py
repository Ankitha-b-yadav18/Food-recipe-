# FoodGPT – AI Powered Food Assistant

```python
import random

print("=" * 50)
print("🍽️ Welcome to FoodGPT")
print("Your Personal AI Food Assistant")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user = input("\nYou: ").lower()

    if user == "exit":
        print("FoodGPT: Thank you for using FoodGPT. Have a healthy day! 😊")
        break

    elif "breakfast" in user:
        print("FoodGPT: I recommend Idli, Dosa, Oats, Upma, or a Vegetable Sandwich for breakfast.")

    elif "lunch" in user:
        print("FoodGPT: A balanced lunch can include Rice, Dal, Vegetables, Roti, and Salad.")

    elif "dinner" in user:
        print("FoodGPT: For dinner, try Chapati with Curry, Paneer, Soup, or Grilled Chicken.")

    elif "healthy" in user:
        print("FoodGPT: Fruits, vegetables, nuts, sprouts, and whole grains are excellent healthy food choices.")

    elif "weight loss" in user:
        print("FoodGPT: Focus on high-protein foods, vegetables, fruits, and reduce sugary foods.")

    elif "weight gain" in user:
        print("FoodGPT: Include milk, bananas, nuts, eggs, rice, and protein-rich foods in your diet.")

    elif "protein" in user:
        print("FoodGPT: Good protein sources include Eggs, Paneer, Chicken, Fish, Soybeans, and Lentils.")

    elif "recipe" in user:
        print("FoodGPT: Tell me the ingredients you have, and I will suggest a recipe.")

    elif "pizza" in user:
        print("FoodGPT: Pizza is a delicious Italian dish made with cheese, sauce, and various toppings.")

    elif "burger" in user:
        print("FoodGPT: Burgers are popular fast-food items served with patties and vegetables.")

    else:
        responses = [
            "Please ask me about food, recipes, nutrition, or healthy eating.",
            "I can help with meal plans, recipes, and nutrition information.",
            "Ask me about breakfast, lunch, dinner, calories, or healthy foods."
        ]
        print("FoodGPT:", random.choice(responses))
```
