class Room(object):

    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.path={}

    def go(self,direction):
        return self.paths.get(direction,None)

    def add_paths(self,path):
        self.paths.update(paths)
