class restaurants:
    def __init__(self,name,cousine_type):
        self.name=name
        self.cousine_type=cousine_type
    def desctibe_restaurant(self):
        print(f'restaurant {self.name} has {self.cousine_type} foods' )
    
    def open_restaurant(self):
        print(f'rerestaurant {self.name} is now open')
    
restaurant = restaurants('Anghazi','Japanees')   
restaurant.desctibe_restaurant()
restaurant.open_restaurant()


restaurant2 =restaurants('Kolahaian' , 'hame jore')
restaurant3 =restaurants('akhtari' , 'sag paz!')




