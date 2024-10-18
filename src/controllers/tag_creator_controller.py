from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class CreateTagController:
    '''
        responsabilidade pela implementação de regras de negócios
    '''
    
    def create(self, product_code: str) -> Dict:
        pass 
    
    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag