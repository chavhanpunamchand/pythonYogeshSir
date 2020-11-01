from prodopsmemory import *
from persistinfile import *

operations = {
    1:  add_product,
    2 : update_product,
    3 : delete_product,
    4 : get_product,
    5 : get_all_products,
    6 : add_product_infile,
    7 : update_product_in_file,
    8 : delete_product_from_file,
    9 : get_single_product_from_file,
    10 : get_all_products_from_file
}


while True:

    print('''
            # In Memory
            1. Add Product
            2. Update Product
            3. Delete Product
            4. Get Product
            5. Get All Products
            # In File
            6. Add Product
            7. Update Product
            8. Delete Product
            9. Get Product
            10. Get All Product
    ''')

    choice = int(input('Enter Your Choice : '))
    funref = operations.get(choice)
    if funref:
       result =  funref()
       print(result)
    else:
        print('Invalid Choice..!')

    ch = input('Do you want to continue.. [yes,y] : ')
    if ch.lower() not in ['yes','y']:
        break





