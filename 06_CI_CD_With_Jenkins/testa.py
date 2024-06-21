def tryLambda():
    our_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    new_list = filter((lambda x: x / 2 == 0), our_list)
    print(list(filter(lambda x: x % 2 == 0, our_list)))
    print(new_list)

tryLambda()


class MyClass():
    
    def __init__(self, artifact, packet, shell) -> None:
        self.artifact = artifact
        self.packet = packet
        self.shell = shell


    @classmethod
    def from_string(cls, string):
        artifact, packet, shell = string.split(',')
        return cls(artifact, packet, shell)
    
    def __str__(self) -> str:
        return f'{self.artifact}, {self.packet}, {self.shell}'
    
    def __repr__(self) -> str:
        return f'{self.artifact}, {self.packet}, {self.shell}'
    

