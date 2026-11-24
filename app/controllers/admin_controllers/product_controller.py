from app.services import product_service

def get_products():
    return {
        "allProducts" : "all products found"
    }

def create_product(data):
    return product_service.create_product(data)

def update_product():
    return {
        'product updated' : "udpated successfully"
    }

def delete_product():
    return {
        'deleted' : 'deleted succesffully'
    }