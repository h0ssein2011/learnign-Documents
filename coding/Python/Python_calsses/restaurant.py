class restaurants:
    
    def __init__(self,name,cousine_type):
        self.name=name
        self.cousine_type=cousine_type
        self.number_served = 0

    def desctibe_restaurant(self):
        print(f'restaurant {self.name} has {self.cousine_type} foods' )
    
    def open_restaurant(self):
        print(f'rerestaurant {self.name} is now open')
    
    def set_number_served(self,amount): 
        self.number_served = amount
    
    def increments_number_served(self,new_amount):
        self.number_served += new_amount



restaurant = restaurants('Anghazi','Japanees')   
restaurant.desctibe_restaurant()
restaurant.open_restaurant()
print(f'this restaurant can server: {restaurant.number_served} person')
restaurant.number_served = 442
print(f'this restaurant can server: {restaurant.number_served} person')
restaurant.set_number_served(50)
print(f'this restaurant can server: {restaurant.number_served} person')
restaurant.increments_number_served(150)
print(f'this restaurant can server: {restaurant.number_served} person')


restaurant2 =restaurants('Kolahaian' , 'hame jore')
restaurant3 =restaurants('akhtari' , 'sag paz!')




