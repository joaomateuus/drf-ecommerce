# from data.login import LoginScript
# instance = LoginScript()
import pandas as pd
from core import models


class PopulateDb:
    def __init__(self) -> None:
        self.csv_path = '../data/gamestop_data_formatted.csv'
        self.categories_id = {}
        self.subcategories_id = {}
        
    def create_category(self, name: str):
        exists = models.ProductCategory.objects.filter(
            name=name
        ).exists()
        if exists: return
        
        category = models.ProductCategory.objects.create(
            name=name
        )
        return category.id
    
    def create_subcategory(self, name: str, parent_id: int):
        pass
    
    def create_brand(self, name: str):
        pass
    
    def create_product(
        product_name: str,
        product_desc: str,
        sku: str,
        sub_category_id: int,
        brand_id: int,
        quantity: int,
        image_url: str
    ):
        pass
        
    def main(self):
        df_games = pd.read_csv(self.csv_path, engine='python')
        
        for _, game in df_games.iterrows():
            category = game.get('category')
            sub_category = game.get('sub_category')
            brand = game.get('brand')
            
            category_id = self.create_category(category)
            if not category_id:
                category_id = models.ProductCategory.objects.filter(
                    name=category
                ).first().id
            
            sub_category_id = self.create_subcategory(sub_category, category_id)
            if not sub_category_id:
                sub_category_id = models.ProductSubCategory.objects.filter(
                    name=sub_category
                ).first().id
                
            brand_id = self.create_brand(brand)
            if not brand_id:
                brand_id = models.Brand.objects.filter(
                    name=brand
                ).first().id
            
            
            
            
instance = PopulateDb()
instance.main()      
    
    