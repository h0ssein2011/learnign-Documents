class user:
    def __init__(self,first_name,last_name,age,gender,password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.password = password
        self.login_attemps = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is {self.age} years old and a {self.gender}')
    
    def greeting(self):
        print(f'Hello {self.first_name} {self.last_name}')
    
    def increment_loggin_attemps(self):
        self.login_attemps += 1
    
    def reset_login_attemps(self):
        self.login_attemps = 0
    


Ali = user('Ali','Ahmadi',36 , 'mard',12345)
Reza = user('Reza','Yavari',20 , 'mard',123456)
Simin = user('Simin','tabatabaei',29 , 'Zan',1234567)

Ali.describe_user()
Ali.greeting()
Ali.increment_loggin_attemps()
Ali.increment_loggin_attemps()
Ali.increment_loggin_attemps()
print(Ali.login_attemps)
Ali.reset_login_attemps()
print(Ali.login_attemps)


Reza.describe_user()
Reza.greeting()

Simin.describe_user()
Simin.greeting()