from flask_app import app, render_template, request, redirect, session
from flask_app.models.recipe import Recipe


#! CREATE
@app.route('/recipe/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new_recipe.html')

@app.route("/recipe/create", methods = ['post'])
def create_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/new')
    Recipe.save(request.form)
    return redirect('/recipes')

#! READ ALL
@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html', recipes = Recipe.get_all())