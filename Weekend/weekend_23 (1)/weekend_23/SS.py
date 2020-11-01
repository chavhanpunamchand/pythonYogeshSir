class A:

    def __init__(self):
        self.x = 10     # instance          --> normal instance variable
        self._y=20      #instnace   _       --> restricted ---> protected
        self.__z=30     #instance   __      --> more restricted --> private

a = A()
print('Changing using --> SS -->',a.__dict__)
