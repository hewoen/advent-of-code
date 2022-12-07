MAX_SIZE = 100000 

class File:
    def __init__(self,name,size):
        self._name = name
        self._size = size
        
    @property
    def name(self):
         return self._name
     
    @property
    def size(self):
         return self._size

class Directory:
     def __init__(self,name,predecessor=None):
         self._elements = {}
         self._name = name
         if predecessor is not None:
             self._elements.update({"..":predecessor})
         
     @property
     def name(self):
         return self._name
     
     @property
     def size(self):
         size = 0
         for name,element in self._elements.items():
             if name!="..":
                size = size + element.size
         return size
     
     def add_object(self,obj):
         if(obj.name not in self._elements.keys()):
            self._elements.update({obj.name:obj})

     def get_object(self,name):
        return self._elements.get(name)
    
     @property
     def objects(self):
         return self._elements.items()
        

filesystem = Directory("/")
current_directory = filesystem

with open("input.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        line = line.strip().replace("\n","")
        cmd = line.split(" ")
        if cmd[0]=="$" and cmd[1]=="cd":
            if cmd[2]=="/":
                current_directory = filesystem
            else:
                current_directory.add_object(Directory(cmd[2],current_directory))
                current_directory = current_directory.get_object(cmd[2]) 
        elif cmd[0]=="dir":
            current_directory.add_object(Directory(cmd[1],current_directory))
        elif cmd[1]!="ls":
            current_directory.add_object(File(cmd[1],int(cmd[0])))
  
  
  
solution = 0       

def get_size(directory):
    size  = directory.size
    if size > MAX_SIZE:
        size = 0
    for name,object in directory.objects:
        if name == "..":
            continue
        if isinstance(object,Directory):
            size = size + get_size(object) 
            pass
              
    return size

solution = get_size(filesystem)
print("Solution: " + str(solution))