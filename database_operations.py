from sqlalchemy import create_engine
from models import Base
from controller import RecipeController
from views import RecipeView
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///recipes.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

recipe_controller = RecipeController()

recipe_controller.add_recipe(session, "Борщ", "Иванова Мария", "Первое блюдо", "Очень вкусный борщ", "https://www.youtube.com/borsh_recipe", "Свекла, картошка, мясо", "Украинская")

recipes = recipe_controller.get_all_recipes(session)
recipe_view = RecipeView()

for recipe in recipes:
    recipe_view.display_recipe(recipe)