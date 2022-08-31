# Functions are object and we can add pass them trough other obkects(Functions)
def call_user(clinent_name,VIP=False):
    def wisper():
        return clinent_name.lower()+'!'
    def yell():
        return clinent_name.upper()+'!'
    if VIP:
        return yell
    else :
        return wisper

print(call_user('ali')())
print(call_user('Sara',VIP=True)())
