import numpy
import random
import matplotlib.pyplot as plt

node_types = ["tag","anchor","gateway"]



class NetworkGod:
    """Primary interface for interacting with nodes and networks"""
    def __init__(self):
        self.network_list = []
    
    def addNetwork(self,net):
        self.network_list.append(net)

class Node:
    def __init__(self,type,id,name):
        self.name = name
        self.node_type = type
        self.node_id = id
        self.pos = (0,0,0)
        self.history = []

class SimulatedNode(Node):
    def __init__(self,type,id,name):
        super().__init__(type,id,name)
        
        self.history = simulatedData

class Network:
    """Primary interface for 
    """
    def __init__(self,types):
        self.available_types = types
        self.node_count_by_type = dict(zip(node_types, [0]*len(node_types)))
        self.node_list = []
    
    def addNode(self,type,id,name):
        assert type in self.available_types

        self.node_list.append(Node(type,id,name))
        # update counter dict
        #check if exists...
        #self.node_count_by_type[node.type] = self.node_count_by_type[node.type]+1

    def getNodeCount(self,type):
        # get count of nodes based on type

    def updateNodePosition(NodeName):
        # look for node with this name
            # update its position




class Network:
    def __init__(self):
        # KV pair = Type : count
        self.node_count_by_type = dict(zip(node_types, [0]*len(node_types)))
        self.node_id_list = []
    
    def __repr__(self):
        return f'Node count {Network.node_count_by_type}, print speed = {Network.update_rate}'

class Node(Network):
    #TODO name can have a function that assigns a node to a specific person or their system ID
    def __init__(self,node_type_list,node_type,node_id,name):
        super().__init__(self)
        
        #TODO how to refer to a specific network here (e.g. stadium, concert_venue)
        assert node_type in Network.node_types
        Network.node_count_by_type[node_type]+=1
        Network.update_rate = 10/Network.node_count_by_type["tag"] #sum(Network.node_count_by_type.values())
        Network.node_id_list.append(node_id)
        
        self.name = name
        self.type = node_type
        self.id = node_id
        self.active = False
        self.position = numpy.array([0,0,0])
        self.position_history = []
        
    def __repr__(self):
        return f'Node type: {self.type}, located at {self.position}.'
    
    def update_position(self, position):
        self.position = position
        self.position_history.append(list(self.position))
        


class SimulatedNode:
    def __init__(self,node_type,node_id,name):
        #TODO how to refer to a specific network here (e.g. stadium, concert_venue)
        assert node_type in Network.node_types
        Network.node_count_by_type[node_type]+=1
        Network.update_rate = 10/Network.node_count_by_type["tag"] #sum(Network.node_count_by_type.values())
        Network.node_id_list.append(node_id)
        
        self.type = node_type
        self.id = node_id        
        self.active = False
        self.position = numpy.array([0,0,0])
        self.position_history = [] #TODO prepend history
        
    def __repr__(self):
        return f'Node type: {self.type}, located at {self.position}.'
    
    def get_random_position_updates(self):
        """
        Random walk simulation implementation
        """
        self.active = True
        def get_random_increment():
            return [numpy.random.normal(),numpy.random.normal(),numpy.random.normal()]
        
        random_increment = get_random_increment()
        self.position = self.position+random_increment
        self.position_history.append(list(self.position))
        return self.position

def get_position_history(tag_id,get_just_values=False):
    x = numpy.asarray(tag_id.position_history)[:,0]
    y = numpy.asarray(tag_id.position_history)[:,1]
    
    if get_just_values:
        return x,y
    
    else:
        plt.plot(x,y)
        plt.show()

tags_list = ["TI:PS:LA:LA:PO:EH",
            "TI:PS:LA:LA:PO:EL",
            "TI:PA:LA:LA:PO:EL",
            "TI:AD:LA:LA:PO:EL",
            "TI:PS:GG:LA:PO:EL",
            "ZI:PS:LA:LA:PO:EL",
            "ZI:PA:LA:LA:PO:EL",
            "ZI:AD:LA:LA:PO:EL",
            "ZI:PS:GG:LA:PO:EL"]

# if __name__ == "__main__":    
#     simulated_tags = {tags_list[idx]: SimulatedNode('tag',tags_list[idx],name=f'tag{idx}') for idx in range(len(tags_list))}
#     detected_tags = {}
    
#     for _ in range(2000):
#         received_id = numpy.random.choice(tags_list)
#         received_position = simulated_tags[received_id].get_random_position_updates()
#         received_packet = {"tag_ID": received_id, "position_data": received_position}
#         if received_packet["tag_ID"] not in detected_tags.keys():
#             detected_tags[received_packet["tag_ID"]] = Node("tag", received_packet["tag_ID"], name=received_packet["tag_ID"])
#         detected_tags[received_packet["tag_ID"]].update_position(received_position)        
    
    
#     for tag in detected_tags.values():
#         x,y = get_position_history(tag,get_just_values=True)
#         plt.plot(x,y)
#     plt.show()
    
#     for tag in simulated_tags.values():
#         x,y = get_position_history(tag,get_just_values=True)
#         plt.plot(x,y)
#     plt.show()
