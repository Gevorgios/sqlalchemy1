# Этот файл для контроллера, который будет соединять модель и представление
from models import Recipe
from sqlalchemy.orm import sessionmaker

class RecipeController:
    def add_recipe(self, session, name, author, recipe_type, description, video_link, ingredients, cuisine):
        new_recipe = Recipe(name=name, author=author, recipe_type=recipe_type, description=description, video_link=video_link, ingredients=ingredients, cuisine=cuisine)
        session.add(new_recipe)
        session.commit()

    def get_all_recipes(self, session):
        return session.query(Recipe).all()