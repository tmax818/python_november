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

#! READ ONE

@app.route('/recipes/<int:id>')
def show_recipe(id):
    data = {'id': id}
    return render_template('show_recipe.html', recipe = Recipe.get_one(data))

#! UPDATE

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    data = {'id': id}
    return render_template('edit_recipe.html', recipe = Recipe.get_one(data))

@app.route("/recipes/update", methods = ['post'])
def update_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{request.form['id']}")
    Recipe.update(request.form)
    return redirect('/recipes')

#! DELETE

@app.route('/recipes/destroy/<int:id>')
def destroy_recipe(id):
    data = {'id': id}
    Recipe.destroy(data)
    return redirect('/recipes')