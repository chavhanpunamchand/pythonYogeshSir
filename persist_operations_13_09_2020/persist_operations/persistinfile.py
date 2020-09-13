from prodopsmemory import *
from product import Product
                                        #lang obj --> file --> serialization
                                    # here --> python object-> into file --> serialization
def write_productsinto_file(prod):      # to save product inside file
    with open('products.txt','a+') as file:
        prodasstr = str(prod.prodId)+"\t\t"+prod.prodName+"\t\t"+str(prod.prodQty)+"\t\t"+str(prod.prodPrice)+"\t\t"+prod.prodRemarks
        file.writelines(prodasstr+"\n")

                            #file content --> lang object
                            #file content --> python object -->
def read_products():        # fetch all products into list      --> all products -->read
    file_products = []
    try:
        with open('products.txt', 'r') as file:
            products = file.readlines()
            products = [prod.strip() for prod in products]
            for prod in products:
                prod = prod.split("\t\t")
                file_products.append(Product(prod[0],prod[1],prod[3],prod[2],prod[4]))
    except:
        pass
    return file_products


def checkfor_product_file(pid):     # u pass on id --> this function will check --> do we have product inside -- file--> if present-- will return
    try:
        with open('products.txt', 'r') as file:
            products = file.readlines()
            for prod in products:
                prod = prod.split("\t\t")
                if int(prod[0])==pid:       #pid,pnm,prc,pqty,prem      101		XXX		22		828.23		XX
                    return Product(prod[0],prod[1],prod[3],prod[2],prod[4])
    except:
        pass



def add_product_infile():
    prod = get_user_input(0)
    fileprod = checkfor_product_file(prod.prodId)
    if fileprod:
            return "Duplicate Product"
    else:
        write_productsinto_file(prod)
        return "Product Added into File"

def get_all_products_from_file():
    return read_products()

def delete_product_from_file():
    pid = get_product_id_input()        # take id input from user
    fileprod = checkfor_product_file(pid)   #--> check that prod is present inside file
    if fileprod:        # if present inside file
        allproducts = read_products()       # read all products from file   --> get all products from file  []
        allproducts.remove(fileprod)        # will remove that product from list        --> list madhn --remove that product
        with open('products.txt', 'w') as file:     # new file--> old wali delete
            for prod in allproducts:            #[except that product]  --> iterat -> except that product--> all products
                prodasstr = str(prod.prodId) + "\t\t" + prod.prodName + "\t\t" + str(prod.prodQty) + "\t\t" + str(
                prod.prodPrice) + "\t\t" + prod.prodRemarks
                file.writelines(prodasstr + "\n")
                return 'Product removed Successfully..!'
    return "No Product Present cannot remove..!"

def get_single_product_from_file():
    pid = get_product_id_input()
    return checkfor_product_file(pid)


def update_product_in_file():
    pid = get_product_id_input()  # take id input from user
    fileprod = checkfor_product_file(pid)  # --> check that prod is present inside file
    if fileprod:  # if present inside file
        allproducts = read_products()
        allproducts.remove(fileprod)
        prod = get_user_input(pid)  # take new values from user
        fileprod.prodQty = prod.prodQty     # new value -- old product la
        fileprod.prodName = prod.prodName
        fileprod.prodPrice= prod.prodPrice
        fileprod.prodRemarks = prod.prodRemarks
        allproducts.append(fileprod)        #fileprod --new values
        with open('products.txt', 'w') as file:  # new file--> old wali delete
            for prod in allproducts:  # [except that product]  --> iterat -> except that product--> all products
                prodasstr = str(prod.prodId) + "\t\t" + prod.prodName + "\t\t" + str(prod.prodQty) + "\t\t" + str(
                    prod.prodPrice) + "\t\t" + prod.prodRemarks
                file.writelines(prodasstr + "\n")
                return 'Product Updated Successfully..!'
    return "No Product Present cannot Update..!"

