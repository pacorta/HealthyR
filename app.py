from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

#@app.route('/form', methods=['GET', 'POST'])
#def form():
#    if request.method == 'POST':
#        restrictions = request.form.getlist('restrictions')
#        meal = generate_meal(restrictions)
#        return render_template('meal.html', meal=meal['name'], video_url=meal['video_url'])
#    return render_template('dietary_restrictions.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        restrictions = request.form.getlist('restrictions')
        meal = generate_meal(restrictions)
        return render_template('dietary_restrictions.html')


@app.route('/meal', methods=['GET', 'POST'])
def meal():
    if request.method == 'POST':
        restrictions = request.form.getlist('restrictions')
        meal = generate_meal(restrictions)
        return render_template('meal.html', meal=meal['name'], video_url=meal['video_url'])
    

def generate_meal(restrictions):
    meals = [
        {'name': 'Grilled salmon with asparagus', 'restrictions': ['gluten-free', 'nut-free'], 'video_url': 'https://www.youtube.com/embed/Kdq3khk_8n0'},
        {'name': 'Roasted vegetable stir-fry', 'restrictions': ['vegetarian', 'vegan'], 'video_url': 'https://www.youtube.com/embed/h8IXBipqYgs'},
        {'name': 'Spaghetti with meat sauce', 'restrictions': ['nut-free'], 'video_url': 'https://www.youtube.com/embed/yfA94mLU0oo'},
        {'name': 'Carrot Soup', 'restrictions': ['gluten-free', 'nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/embed/4coBVpdCIMQ'},
        {'name': 'Chicken Stroganoff', 'restrictions': ['gluten-free', 'nut-free'], 'video_url': 'https://www.youtube.com/watch?v=5nGg68FnbM4&ab_channel=RecipeTinEats'},
        {'name': 'Quick Chicken Marsala', 'restrictions': ['nut-free',], 'video_url': 'https://www.youtube.com/watch?v=_Nw3bDUpb7Q&ab_channel=NatashasKitchen'},
        {'name': 'Chicken & Spinach Skillet Pasta with Lemon & Parmesan', 'restrictions': ['nut-free', 'gluten-free'], 'video_url': 'https://www.youtube.com/watch?v=So3MmXLYAFA&ab_channel=HealthwithDiet'},
        {'name': 'Spinach & Mushroom Quiche', 'restrictions': ['gluten-free', 'nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/watch?v=Dfsgi5_J2Oc&ab_channel=TastyMeals%26Treats'},
        {'name': 'Chicken Cutlets with Sun-Dried Tomato Cream Sauce', 'restrictions': ['gluten-free', 'nut-free'], 'video_url': 'https://www.youtube.com/watch?v=C6YPhoqfHsg&ab_channel=OnesHealth'},
        {'name': 'One-Pot Garlicky Shrimp & Broccoli', 'restrictions': ['nut-free', 'gluten-free'], 'video_url': 'https://www.youtube.com/watch?v=exuzvgnyECk&ab_channel=SoupedUpRecipes'},
        {'name': 'Vegetable Weight-Loss Soup', 'restrictions': ['gluten-free'], 'video_url': 'https://www.youtube.com/watch?v=escHMukMphc&ab_channel=BrownGirlsKitchen'},
        {'name': 'Shirataki Noodles with Tofu & Veggies', 'restrictions': ['nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/watch?v=qkv_CxkdWB4&ab_channel=YeungManCooking'},
        {'name': 'The Ultimate Vegetarian Club Sandwhich', 'restrictions': ['vegetarian', 'nut-free'], 'video_url': 'https://www.youtube.com/watch?v=j5gg365Ewaw&ab_channel=NOTANOTHERCOOKINGSHOW'},
        {'name': 'Crispy Smashed Potatoes', 'restrictions': ['vegetarian', 'nut-free', 'gluten-free'], 'video_url': 'https://www.youtube.com/watch?v=Ai_kivZXN9o&ab_channel=NatashasKitchen'},
        {'name': 'Creamy Linguine Spinach in a Sun dried Tomato Cream Sauce', 'restrictions': ['nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/watch?v=3NSTpq-la3E&ab_channel=TasteDis'},
        {'name': 'Spinach & Artichoke Dip Pasta', 'restrictions': ['nut-free', 'vegetarian'], 'video_url': 'https://www.youtube.com/watch?v=MS1eAjcp2HU&ab_channel=Mr.MakeItHappen'}
    ]

    available_meals = []
    for meal in meals:
        if all(restriction in meal['restrictions'] for restriction in restrictions):
            available_meals.append(meal)

    if len(available_meals) == 0:
        return 'No meals available with these restrictions'

    return random.choice(available_meals)

if __name__ == '__main__':
    app.run(debug=True)