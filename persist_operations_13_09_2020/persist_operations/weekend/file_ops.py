
from weekend.prodinfo import Product

FILE_NAME = "products.txt"


#write the product objects into file -->
def write_products_into_file(products): #a --> if present -- append -- in case absent --> new create
    with open(FILE_NAME, 'a') as file:  # context manager-->    file might be present or absent
        for prod in products:
            prodstr = str(prod.prodId) + "," + prod.prodName + "," + str(prod.prodPrice) + "," + str(
                prod.prodQty) + "," + prod.prodBarcode + "\n"
            file.writelines(prodstr)

    print('Product Contents written into a file..!')

#read the contents from file -->
def read_products_from_file():
    all_products = []
    try:
         file = open('products.txt','r')  # context manager-->     file might be present or absent
    except FileNotFoundError as er:
        print('File not present -->',er.args)
    else:
        allllines = file.readlines()
        for line in allllines:
            line = line.strip()
            prodcontents = line.split(',')
            all_products.append(
                Product(prodcontents[0], prodcontents[1], prodcontents[2], prodcontents[3], prodcontents[4]))
    finally:
        if file:
            file.close()


    return all_products

