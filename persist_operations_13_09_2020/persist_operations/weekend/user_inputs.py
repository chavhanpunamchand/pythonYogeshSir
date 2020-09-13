from weekend.prodinfo import Product

def get_product_input():    # take input from user and create product and keep in inside list--> No --> return entire list
    products = []  #
    count = 1
    while True :
        pid = int(input('Enter Product Id :'))
        pnm = input('Enter Product Name : ')
        pqty = int(input('Enter Product Qty :'))
        price = float(input('Enter Product Price : '))
        pbar = input('Enter Product BarCode : ')
        p1 = Product(pid=pid,pnm=pnm,prc=price,pqt=pqty,pbar=pbar)
        products.append(p1)

        if count%2==0:
            choice = input('Do you want to continue [n/no]')
            if choice.lower() in ['n','no']:
                break              # break cha meaning
        count = count + 1
    return products
