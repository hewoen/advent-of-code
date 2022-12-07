AVAILABLE_SPACE = 70000000

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
  

total_size = filesystem.size
setpoint_size = 30000000-(AVAILABLE_SPACE-total_size)
  
solution = 0       

def get_size(directory):
    dirs = []
    for name,object in directory.objects:
        size = object.size
        if name != ".." and isinstance(object,Directory) and setpoint_size <= size:
            dirs.append(size) 
            dirs = dirs + get_size(object)
               
    return dirs
dirs = get_size(filesystem)
solution = min(dirs)
print("Solution: " + str(solution))