'''
Exception --> condition /event --> normal program execution --> interrupt-->
            --> keywords -->
        1                try
                                        code which might generate exeption          --> proper
        2                except
                                    --> code to handle that situation/event/condition   --> proper
        3                else
                                    --> if try is successful then only else will be executed
        4                finally
                                    --> u shud write --> code which resource clean up activaties..
                                        always--> let the excep / not
                        2* --> can be many
        12
        123
        1234                        1   2  3    4
        14                          1^  2  -    4
                                    1   -  3    4
        124

        1       2         3         4               --> seq shud be this
        1                           4
        1       2
        1       2         2         2*
        1       2         3
        1       2          2        2*      3
        1       2          2        2*      4
        1       2          2        2*      3       4
        1        2          4



        1-3 only - not allowed
        always 1 pahije
        1 --> 2/4
        1 -->2*/3/4

'''

from weekend.user_inputs import get_product_input
from weekend.file_ops import write_products_into_file,read_products_from_file



print('''
        1. Write Products into File
        2. Read Products From File
''')


operations = {
            1 : write_products_into_file,
            2 : read_products_from_file
}
choice = int(input('Enter Ur Choice : '))
funref = operations.get(choice)
if funref:
    if choice==1:
        products = get_product_input()
        funref(products)
    else:
        funref()
