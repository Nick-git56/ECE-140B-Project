#!/usr/bin/python3.9
import random
import numpy
import matplotlib.pyplot as plt
import logging
from scipy.fftpack import diff
from shapely.geometry import Point, Polygon
from descartes.patch import PolygonPatch
import warnings
from shapely.errors import ShapelyDeprecationWarning
from sympy import differentiate_finite
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning) 
# import RFID

# create logger
logger = logging.getLogger('network_manager')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

NODE_TYPES = ["tag","anchor","gateway"]
SECTION_TYPES = ["suite","bathroom","vendor","commons"]
RESOURCE_PATH = "media/"

SIM_BRACELET_DICT = {"TI:PS:LA:LA:PO:EH":"[45, 27, 129, 56]",\
                    "TA:PS:LG:LA:PO:EF":"[45, 27, 19, 56]",\
                    "TI:PS:ER:LA:PO:EF":"[45, 27, 129, 59]"
                    }
BRACELET_DICT = {"TI:PS:LG:LA:PO:EH":"[45, 227, 129, 56]",\
                 "TI:PS:LG:LA:PO:EF":"[99, 197, 79, 28]"
                }
BRACELET_DICT.update(SIM_BRACELET_DICT)

class NetworkManagner:
    """
    Primary interface for interacting with nodes and networks
    """
    def __init__(self):
        self.network_dict = {}
    
    def add_network(self,name):
        #assert name in self.network_dict.keys()
        self.network_dict[name] = Network(NODE_TYPES,SECTION_TYPES,name)
        return self.network_dict[name]

    def node_count_by_type(self,network,node_type):
        return network.node_count_by_type[node_type] 

class Network:
    """
    
    """
    def __init__(self,node_types,section_types,name):
        self.node_types = node_types
        self.section_types = section_types
        self.network_name = name
        self.node_dict = {type: {} for type in self.node_types}
        self.section_dict = {type: {} for type in self.section_types}
        logger.info(f"Created network '{name}'")

    def __repr__(self):
        node_dict_info = {node_type:len(self.node_dict[node_type]) for node_type in self.node_types}
        return f"Network Name:\t\t{self.network_name}\nNode Count by Type:\t{node_dict_info}"

    def add_section(self,section_type,name,vertex_list,color='blue',vendor='None'):
        assert section_type in self.section_types, "Not an available type"
        assert name not in self.section_dict[section_type]
        self.section_dict[section_type][name] = Section(section_type,name,vertex_list,color,vendor)
        logger.info(f"Added {section_type} {name} to the {self.network_name} network")

    def delete_section(self,section_type,name):
        assert section_type in self.section_types, "Not an available type"
        assert name not in self.section_dict[section_type]
        del self.section_dict[section_type][name]
        logger.info(f"Removed {section_type} {name} from the {self.network_name} network")


    def node_count_by_type(self,node_type):
        return len(self.node_dict[node_type])
    
    def get_node_name(self, node_type, node_id):
        return self.node_dict[node_type][node_id].name

    def add_node(self,node_type,node_id,name=None,position=None,color=None,section=None,products=None):
        assert node_type in self.node_types, "Not an available type"
        assert node_id not in self.node_dict[node_type].keys(), "ID already in use"
        if node_type == "tag":
            if not position:
                position = numpy.zeros(3)
            self.node_dict[node_type][node_id] = Tag(node_type,node_id,name,self,position,color)
            self.update_rate = 10/self.node_count_by_type("tag")
        elif node_type == "anchor":
            if not position:
                position = numpy.asarray([float(item) for item in input("Enter x,y,z [m]: ").split()])
            self.node_dict[node_type][node_id] = Anchor(node_type,node_id,name,self,position,color)
        elif node_type == "gateway":
            if not position:
                position = numpy.asarray([float(item) for item in input("Enter x,y,z [m]: ").split()])
            self.node_dict[node_type][node_id] = Gateway(node_type,node_id,name,self,position,color,section,products)

        logger.info(f"Added {node_type} {node_id} ({name}) to the {self.network_name} network")
        return self.node_dict[node_type][node_id]

    def remove_node(self,node_type,node_id,name=None):
        assert node_type in self.node_types
        try:
            del self.node_dict[node_type][node_id]
            logger.info(f"Removed {node_type} {node_id} ({name}) from the {self.network_name} network")
            if node_type == "tag":
                self.update_rate = 10/self.node_count_by_type("tag")

        except KeyError:
            logger.warning(f"Operation failed: could not find {node_id} in the network")
    
    def activate(self,node_type,node_id,name=None):
        self.node_dict[node_type][node_id].activate()

    def deactivate(self,node_type,node_id,name=None):
        self.node_dict[node_type][node_id].deactivate()

class Section:
    def __init__(self,section_type,name,vertex_list,color='blue',vendor=None):
        self.type = section_type
        self.name = name
        self.color = color
        self.shape = Polygon(vertex_list)
        self.centroid = numpy.array(self.shape.centroid)
        self.vendor = vendor

    def contains(self,position):
        return self.shape.contains(Point(position[0],position[1]))

    def change_center_point(self,position):
        self.centroid = position
    
    # def assign_vendor(self,vendor):
    #     self.vendor = vendor

class Node:
    def __init__(self,node_type,node_id,name,network,simulation=True): #TODO: on top of the file in settings, simulation setting is on by default
        self.type = node_type
        self.id = node_id
        self.name = name
        self.network = network
        self.simulated = simulation

    def __repr__(self):
        return f"{self.name} ({self.type})"

    def activate(self):
        self.active = True
        logger.info(f"Activated {self.type} {self.id} ({self.name}), {self.network.network_name} network")

    def deactivate(self):
        self.active = False
        logger.info(f"Deactivated {self.type} {self.id} ({self.name}), {self.network.network_name} network")

    def get_position(self):
        if self.type == "tag":
            if self.simulated:
                self.sim_update_position()
            else:
                self.update_position()
        return self.position[0],self.position[1]

    def get_position_history(self):
        return numpy.asarray(self.position_history)[:,0], numpy.asarray(self.position_history)[:,1]

class Tag(Node):

    def __init__(self,node_type,node_id,name,network,position=numpy.zeros(3),color=None,map=None):
        super().__init__(node_type,node_id,name,network)
        self.active = False
        self.position = position
        self.position_history = [list(self.position)]
        self.transaction_history = []
        self.objective = None

        if not color:
            self.color = 'blue'
        else:
            self.color = color
            
    def update_position(self):
        #TODO: UWB_BLE code goes here
        # self.position = position
        # self.position_history.append(list(self.position))
        pass

    def sim_update_position(self):
        #TODO: first change_objective gets called during a position update so the gateway update has to go after position updates. Make more flexible
        def change_objective():
            sample = random.uniform(0,1)
            initial_distribution=numpy.array([[0.2,0.5,0.3]])
            probability_ranges = numpy.cumsum(initial_distribution)

            for i in range(len(probability_ranges)):
                if probability_ranges[i] > sample:
                    return list(self.network.section_dict['vendor'].values())[i]

        if not self.objective:
            self.objective = change_objective()

        if self.objective.contains(self.position):
            #i.e. when you arrive to the destination, change it
            self.objective = change_objective()

        def get_random_increment(destination):
            difference_vector = self.position[:2]-destination
            difference_vector = difference_vector/numpy.linalg.norm(difference_vector)
            return numpy.asarray([0.1*numpy.random.normal(difference_vector[0],scale=0.3),0.1*numpy.random.normal(difference_vector[1],scale=0.3),0])
        random_increment = get_random_increment(self.objective.centroid)
        self.position += random_increment

        #TODO:hardcoded = bad
        if self.position[0] < 0 or self.position[1] < 0 or self.position[0]>10 or self.position[1]<5:
            self.position -= random_increment*2

        self.position_history.append(list(self.position))
        return self.position
    
class Anchor(Node):

    def __init__(self,node_type,node_id,name,network,position,color=None):
        super().__init__(node_type,node_id,name,network)
        self.active = True
        self.position = position
        self.position_history = [list(self.position)]
        if not color:
            self.color = 'red'
        else:
            self.color = color

class Gateway(Node):
    def __init__(self,node_type,node_id,name,network,position,color=None,section=None,products=None):
        super().__init__(node_type,node_id,name,network)
        self.name = name
        self.position = position
        if not color:
            self.color ='green'
        else:
            self.color = color
        self.network = network
        self.section = section
        self.active = True
        self.products = products
        #TODO:integrate Gateway class better with Gateway module
        # self.scanner = RFID.Reader(self.active)
        self.transaction_history = []

    def get_most_recent_transaction(self):
        if self.transaction_history:
            return self.transaction_history[-1]
        else:
            return None

    def get_updates(self):
        if self.simulated:
            tag_id = random.choice(list(SIM_BRACELET_DICT.keys()))
            tag = self.network.node_dict["tag"][tag_id]
            if tag_id not in self.network.node_dict["tag"].keys():
                logger.warning(f"Trying to execute transaction on an untracked tag... Make sure to check them in first!")

            elif tag.objective.contains(tag.position):
                sample = random.uniform(0,1)
                if sample > 0.05:
                    product_name = random.choice(list(self.products.keys()))
                    self.record_transaction(tag.id,product_name,self.products[product_name])
                    return True
            else:
                return False

        else:
            raise NotImplementedError
        """ IMPORTANT CODE: DON'T DELETE
        elif not self.simulated:
            if not self.scanner.previous_RFID == self.scanner.new_RFID and self.active:
                self.scanner.previous_RFID = self.scanner.new_RFID
                print(f"Found a new person: {self.scanner.new_RFID}!")
                product_name = random.choice(list(self.products.keys()))
                self.record_transaction(tag.id,product_name,self.products[product_name])
                return self.scanner.new_RFID
            elif not self.active:
                print("scanner deactivated")
        """

    def assign_section(self,section):
        self.section

    def check_in(self,tag_id,name=None,color='black'):
        if tag_id not in self.network.node_dict["tag"].keys():
            self.network.add_node(node_type = "tag", node_id = tag_id, name = name, position=self.position, color = color)
        self.network.node_dict["tag"][tag_id].activate()

    def check_out(self,tag_id):
        self.network.node_dict["tag"][tag_id].deactivate()
    
    def record_transaction(self,tag_id,transaction_type,price):
        self.network.node_dict["tag"][tag_id].transaction_history.append({transaction_type:price})
        self.network.node_dict["gateway"][self.id].transaction_history.append({transaction_type:price})
        logger.info(f"Recorded transaction: {transaction_type} - ${price}, {tag_id} ({self.network.get_node_name('tag',tag_id)}) at {self.id} ({self.name}), {self.network.network_name} network")

class Map:
    def __init__(self,network,map_image=None,dimensions=[16,8]):
        self.network = network
        self.dimensions = dimensions
        self.map_image = map_image
        self.node_dict = network.node_dict
        self.section_dict = network.section_dict
        plt.rcParams["figure.figsize"] = self.dimensions
        plt.rcParams["figure.autolayout"] = True
        self.reset()
    
    def plot_section(self,section_type=None,name=None):
        if section_type and name:
            section = self.section_dict[section_type][name]
            self.ax.add_patch(PolygonPatch(section.shape, facecolor=section.color, edgecolor=[0,0,0], alpha=0.2, zorder=2))
        else:
            for type in self.section_dict:
                for section in self.section_dict[type].values():
                    self.ax.add_patch(PolygonPatch(section.shape, facecolor=section.color, edgecolor=[0,0,0], alpha=0.2, zorder=2))
    
    def plot_position(self, node_type=None, node_id=None):
        if node_type and node_id:
            node = self.node_dict[node_type][node_id]
            x,y = node.get_position()
            self.ax.scatter(x,y, s = 50, c=node.color, alpha=0.5,label=f'{node.type} {node.name}')

        else:
            for tag in self.node_dict["tag"].values():
                x,y = tag.get_position()
                self.ax.scatter(x,y, s=50, c=tag.color, alpha=0.5,label=f'Tag {tag.name}')

            for anchor in self.node_dict["anchor"].values():
                x,y = anchor.get_position()
                self.ax.scatter(x,y, s=50, c=anchor.color, marker='v', label=f'Anchor {anchor.name}')
                self.ax.scatter(x,y, s=100000, c='red', alpha=0.1)

            for Gateway in self.node_dict["gateway"].values():
                x,y = Gateway.get_position()
                self.ax.scatter(x,y, s=50, c=Gateway.color, label=f'Gateway {Gateway.name}')
                self.ax.scatter(x,y, s=1000, c='green', alpha=0.1)

    def plot_position_history(self, length=None, node_type=None, node_id=None):

        if node_type and node_id:
            node = self.node_dict[node_type][node_id]
            x,y = node.get_position_history()
            if not length: length=len(x)
            self.ax.scatter(x[-length:],y[-length:], s = 50, c=node.color, alpha=0.5,label=f'{node.type} {node.name}')
            self.ax.scatter(x[-1],y[x[-1]], s = 50, c=node.color, alpha=0.5)

        else:
            for tag in self.node_dict["tag"].values():
                x,y = tag.get_position_history()
                if not length: length=len(x)
                self.ax.plot(x[-length:],y[-length:], c=tag.color, alpha=0.5,label=f'Tag {tag.name}')
                self.ax.scatter(x[-1],y[-1], c=tag.color, alpha=0.5)

            for anchor in self.node_dict["anchor"].values():
                x,y = anchor.get_position()
                self.ax.scatter(x,y, s=50, c=anchor.color, marker='v', label=f'Anchor {anchor.name}')
                self.ax.scatter(x,y, s=100000, c='red', alpha=0.1)

            for Gateway in self.node_dict["gateway"].values():
                x,y = Gateway.get_position()
                self.ax.scatter(x,y, s=50, c=Gateway.color, label=f'Gateway scanner {Gateway.name}')
                self.ax.scatter(x,y, s=1000, c='green', alpha=0.1)
        
    def reset(self):
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(plt.imread(self.map_image), extent=[0, self.dimensions[0], 0, self.dimensions[1]])

    def show(self):
        plt.xlim([0, self.dimensions[0]])
        plt.ylim([0, self.dimensions[1]])
        plt.legend(loc='best')           
        plt.show()
        plt.close()


if __name__=="__main__":
    #init
    net_god = NetworkManagner()
    petco = net_god.add_network("petco park")
    petco_map = Map(petco,map_image=RESOURCE_PATH + "test_map.jpg",dimensions=[10,5])

    #setup
    petco.add_section(section_type = "suite", name = "suite #1", vertex_list = numpy.array([[0,3],[0,5],[2,5],[2,3]]) ,color = 'orange')
    petco.add_section(section_type = "suite", name = "suite #2", vertex_list = numpy.array([[2,3],[2,5],[4,5],[4,3]]) ,color = 'orange')
    petco.add_section(section_type = "bathroom", name = "wc #1", vertex_list = numpy.array([[4,3],[4,5],[5,5],[5,3]]) ,color = 'blue')
    petco.add_section(section_type = "bathroom", name = "wc #2", vertex_list = numpy.array([[5,3],[5,5],[6,5],[6,3]]) ,color = 'blue')
    petco.add_section(section_type = "suite", name = "suite #3", vertex_list = numpy.array([[6,3],[6,5],[8,5],[8,3]]) ,color = 'orange')
    petco.add_section(section_type = "suite", name = "suite #4", vertex_list = numpy.array([[8,3],[8,5],[10,5],[10,3]]) ,color = 'orange')
    #TODO: for now the gateway needs to be declared before the section, fix
    ###


    snack_menu = {"pretzels":12,"chocolate":5,"chips":12}
    bar_menu = {"beer": 10, "drink": 20, "shot":10}
    food_menu = {"chicken": 15,"pizza":25,"burrito":14}

    snack_guy = petco.add_node(node_type = "gateway", node_id = "TI:AA:LA:LA:PO:EH", name = "snack", position=[0.5,2,3.0], color = 'green', products = snack_menu)
    bartender = petco.add_node(node_type = "gateway", node_id = "TI:AA:LA:LA:PO:EG", name = "bar", position=[7,3,3.0], color = 'green', products = bar_menu)
    chef = petco.add_node(node_type = "gateway", node_id = "TI:AA:LA:LA:PO:EE", name = "food", position=[1,2,3.0], color = 'green', products = food_menu)

    petco.add_section(section_type = "vendor", name = "snacks", vertex_list = numpy.array([[0,0],[0,1],[1.5,1],[1.5,0]]) ,color = 'green', vendor=snack_guy)
    petco.add_section(section_type = "vendor", name = "bar", vertex_list = numpy.array([[3,0],[3,0.5],[7,0.5],[7,0]]) ,color = 'green', vendor=bartender)
    petco.add_section(section_type = "vendor", name = "food", vertex_list = numpy.array([[9,0],[9,2],[10,2],[10,0]]) ,color = 'green', vendor=chef)
    ###

    petco.add_node(node_type = "anchor", node_id = "TI:PS:LA:WA:PO:EH", name = "suite 2", position=[2,3,0])
    petco.add_node(node_type = "anchor", node_id = "TI:PS:XD:WA:PO:EH", name = "suite 3", position=[8,2,0])
    petco.remove_node(node_type = "anchor", node_id = "TI:PS:XD:WA:PO:EH", name = "suite 3")
    petco.add_node(node_type = "anchor", node_id = "TI:PS:XD:WA:PO:EH", name = "suite 3", position=[8,3,0])
    petco.add_node(node_type = "anchor", node_id = "TI:PS:XD:WA:PO:EY", name = "bar", position=[5,0,0])
    petco.add_node(node_type = "tag", node_id = "TI:PS:LG:LA:PO:EH", name = "Nick", position=[2,2,3.0], color = "blue")

    petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LG:LA:PO:EH",name="Nick")
    petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LA:LA:PO:EH",name="Karen",color='pink')
    petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LG:LA:PO:EF",name="Marcin",color='black')
    petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TA:PS:LG:LA:PO:EF",name="Raymond",color='blue')
    petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:ER:LA:PO:EF",name="Rusul",color='orange')
    # petco.node_count_by_type("tag")
    # print(petco.update_rate)
    # print(petco)
    # print(petco.node_dict)

    #simulating movements
    trace = 10
    simulation_time = 100
    for timestep in range(simulation_time):
        petco.node_dict['tag']['TI:PS:LA:LA:PO:EH'].sim_update_position()
        petco.node_dict['tag']['TI:PS:LG:LA:PO:EH'].sim_update_position()
        petco.node_dict['tag']['TI:PS:LG:LA:PO:EF'].sim_update_position()
        petco.node_dict['tag']['TA:PS:LG:LA:PO:EF'].sim_update_position()
        petco.node_dict['tag']['TI:PS:ER:LA:PO:EF'].sim_update_position()
        petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].get_updates()
        petco.node_dict['gateway']['TI:AA:LA:LA:PO:EG'].get_updates()
        petco.node_dict['gateway']['TI:AA:LA:LA:PO:EE'].get_updates()
        # if timestep < trace:
        #     petco_map.plot_position_history(length=timestep)
        # else:
        #     petco_map.plot_position_history(length=trace)
        # # petco_map.plot_position()
        # petco_map.plot_section()
        # petco_map.show()
        # petco_map.reset()


    #mapping functions
    petco_map.plot_position_history()
    petco_map.show()
    # petco_map.plot_position()
    # petco_map.show()
    # petco_map.plot_section("bathroom","wc #2")
    # petco_map.plot_section("vendor","snacks")


    # #transactions
    # petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].record_transaction('TI:PS:ER:LA:PO:EF',"food",100)
    # petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].record_transaction('TI:PS:ER:LA:PO:EF',"drinks",100)
    # petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].record_transaction('TI:PS:ER:LA:PO:EF',"cigarettes",100)
    # print(petco.get_node_name('tag','TI:PS:ER:LA:PO:EF'))
    # print(petco.node_dict['tag']['TI:PS:ER:LA:PO:EF'].transaction_history)
    