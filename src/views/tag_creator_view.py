from src.views.http_types.http_request import HttpRequest

class TagCreatorView:
    '''
        responsabilidade para interagir com HTTP
    '''
    
    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]
        
        # lógica de regra de negócio
        
        # retorno http 