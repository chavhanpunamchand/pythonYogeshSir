from product import Product

products = []



def get_user_input(prodId = 0):
    if prodId==0:  # as its true--> will ask for input
        prodId = int(input('Enter Product Id : '))
    prodNm = input('Enter Product Name : ')
    prodQty = int(input('Enter Product Qty :'))
    prodPrice = float(input('Enter ProductPrice :'))
    prodRemarks = input('Enter Product Reviews : ')
    return Product(prodId,prodNm,prodPrice,prodQty,prodRemarks)

def add_product():
    prod = get_user_input(False)
    lprod = get_product(prod.prodId)
    if lprod:
        return "Product Already Present,cannot add"
    else:
        products.append(prod)   #memory
        return "Product Added Successfully..!"




def get_product_id_input():
    pid = int(input('Enter Product Id : '))
    return pid

def get_product(askforpid=0):
    if askforpid==0:
        pid  = get_product_id_input()       # id ??
    for prod in products:
        if prod.prodId == pid:
            return prod


def get_all_products():
    return products


def delete_product():
    pid  = get_product_id_input()   # ask for id input
    prod = get_product(pid)        # wil not ask
    if prod:
        products.remove(prod)
        return "Product Removed.."
    return "Product Not Present so cannot remove"


def update_product():
    pid = get_product_id_input()    # input ?--> id
    prod = get_user_input()
    lprod = get_product(pid)        #no
    if lprod:
        lprod.prodName = prod.prodName
        lprod.prodPrice = prod.prodPrice
        lprod.prodQty = prod.prodQty
        lprod.prodRemarks = prod.prodRemarks
        return "Product record updated.."
    return "Product not present so cannot update..!"


if __name__ == '__main__':
    pass
    #msg = add_product()
    #print(msg)
    #delete_product()
    #get_product()