class RecipeView:
    def display_recipe(self, recipe):
        print(f"Название%: {recipe.name}")
        print(f"Автор: {recipe.author}")
        print(f"Тип рецепта: {recipe.recipe_type}")
        print(f"Описание: {recipe.description}")
        print(f"Ссылка на видео: {recipe.video_link}")
        print(f"Ингриединты: {recipe.ingredients}")
        print(f"Кухня: {recipe.cuisine}")