import os, django
import random
import pandas as pd
from core import models
from django.db import transaction

class PopulateDb:
    def __init__(self) -> None:
        self.csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gamestop_data_formatted.csv')
        
    def create_category(self, name: str) -> 'models.ProductCategory':
        category, _ = models.ProductCategory.objects.get_or_create(
            name=name
        )
        return category
    
    def create_subcategory(self, name: str, parent: models.ProductCategory) -> 'models.ProductSubCategory':
        sub_category, _ = models.ProductSubCategory.objects.get_or_create(
            name=name,
            parent_category=parent,
        )
        return sub_category
    
    def create_brand(self, name: str) -> 'models.Brand':
        brand, _ = models.Brand.objects.get_or_create(
            name=name
        )
        return brand

    def main(self):
        try:
            df_games = pd.read_csv(self.csv_path, engine='python')
        
            for _, game in df_games.iterrows():
                category = game.get('category')
                sub_category = game.get('sub_category')
                brand = game.get('brand')
                
                created_category = self.create_category(category)
                created_sub_category = self.create_subcategory(sub_category, created_category)
                created_brand = self.create_brand(brand)

                product_name = game.get('name')
                product_desc = game.get('description')
                product_img_url = game.get('image_url')
                price = game.get('price')
                quantity = random.randint(100, 1000)
               
                product = models.Product(
                    subcategory=created_sub_category,
                    brand=created_brand,
                    name=product_name,
                    description=product_desc,
                    price=price,
                    quantity=quantity,
                    image_url=product_img_url,
                )
                print(f'{product}')
                print('product added sucessfully \n')
                product.save()
            print('\n')
            print('\n')
            print('Products Table and relateds populated sucessfully')
        except Exception as e:
            print(str(e))


@transaction.atomic()
def run():
    instance = PopulateDb()
    instance.main()      
    
    