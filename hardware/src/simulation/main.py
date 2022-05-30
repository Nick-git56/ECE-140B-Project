# author: Marcin Kierebinski
import numpy
import time
from threading import Thread
# import RFID
from network_manager import *
from server import Server

ENV_NAME = "test"
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



class Environment:
    def __init__(self,network,server):
        self.name = ENV_NAME
        self.thread_dict = {}
        self.network = network
        self.node_dict = self.network.node_dict
        self.server = server
            
    def run(self,**threads):
        for name, thread in threads.items():
            self.thread_dict[name] = thread
            thread.start()
    
    def clean_up(self):
        for thread in self.thread_dict.values():
            thread.join()

    def simulation(self):
        #check people in
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LG:LA:PO:EH",name="Nick")
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LA:LA:PO:EH",name="Karen",color='pink')
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LG:LA:PO:EF",name="Marcin",color='black')
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TA:PS:LG:LA:PO:EF",name="Raymond",color='blue')
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:ER:LA:PO:EF",name="Rusul",color='orange')
        
        # #simulating movements
        # trace = 3
        simulation_time = 10
        for timestep in range(simulation_time):
            position = petco.node_dict['tag']['TI:PS:LA:LA:PO:EH'].sim_update_position()
            position = petco.node_dict['tag']['TI:PS:LG:LA:PO:EH'].sim_update_position()
            position = petco.node_dict['tag']['TI:PS:LG:LA:PO:EF'].sim_update_position()
            position = petco.node_dict['tag']['TA:PS:LG:LA:PO:EF'].sim_update_position()
            position = petco.node_dict['tag']['TI:PS:ER:LA:PO:EF'].sim_update_position()
            transaction = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].get_updates()
            transaction = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EG'].get_updates()
            transaction = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EE'].get_updates()

############GOOD PLACE TO INSERT RECORDS #####################
            # server.insert_something()

            # if timestep < trace:
            #     petco_map.plot_position_history(length=timestep)
            # else:
            #     petco_map.plot_position_history(length=trace)
            # petco_map.plot_section()
            # petco_map.show()
            # petco_map.reset()

        #finish off with full position history
        # petco_map.plot_position_history()
        # petco_map.show()

if __name__ == "__main__":
    #init
    server = Server()
    net_god = NetworkManagner()
    petco = net_god.add_network("petco park")
    petco_map = Map(petco,map_image=RESOURCE_PATH + "test_map.jpg",dimensions=[10,5])
    env = Environment(petco,server)

    #adding sections
    petco.add_section(section_type = "suite", name = "suite #1", vertex_list = numpy.array([[0,3],[0,5],[2,5],[2,3]]) ,color = 'orange')
    petco.add_section(section_type = "suite", name = "suite #2", vertex_list = numpy.array([[2,3],[2,5],[4,5],[4,3]]) ,color = 'orange')
    petco.add_section(section_type = "bathroom", name = "wc #1", vertex_list = numpy.array([[4,3],[4,5],[5,5],[5,3]]) ,color = 'blue')
    petco.add_section(section_type = "bathroom", name = "wc #2", vertex_list = numpy.array([[5,3],[5,5],[6,5],[6,3]]) ,color = 'blue')
    petco.add_section(section_type = "suite", name = "suite #3", vertex_list = numpy.array([[6,3],[6,5],[8,5],[8,3]]) ,color = 'orange')
    petco.add_section(section_type = "suite", name = "suite #4", vertex_list = numpy.array([[8,3],[8,5],[10,5],[10,3]]) ,color = 'orange')
    
    snack_menu = {"pretzels":12,"chocolate":5,"chips":12}
    bar_menu = {"beer": 10, "drink": 20, "shot":10}
    food_menu = {"chicken": 15,"pizza":25,"burrito":14}
    #TODO: for now the gateway needs to be declared before the section, fix   
    #adding scanners
    snack_guy = petco.add_node(node_type = "gateway", node_id = "TI:AA:LA:LA:PO:EH", name = "snack", position=[0.5,2,3.0], color = 'green', products = snack_menu)
    bartender = petco.add_node(node_type = "gateway", node_id = "TI:AA:LA:LA:PO:EG", name = "bar", position=[7,3,3.0], color = 'green', products = bar_menu)
    chef = petco.add_node(node_type = "gateway", node_id = "TI:AA:LA:LA:PO:EE", name = "food", position=[1,2,3.0], color = 'green', products = food_menu)

    #adding vendor sections
    petco.add_section(section_type = "vendor", name = "snacks", vertex_list = numpy.array([[0,0],[0,1],[1.5,1],[1.5,0]]) ,color = 'green', vendor=snack_guy)
    petco.add_section(section_type = "vendor", name = "bar", vertex_list = numpy.array([[3,0],[3,0.5],[7,0.5],[7,0]]) ,color = 'green', vendor=bartender)
    petco.add_section(section_type = "vendor", name = "food", vertex_list = numpy.array([[9,0],[9,2],[10,2],[10,0]]) ,color = 'green', vendor=chef)

    #adding anchors
    petco.add_node(node_type = "anchor", node_id = "TI:PS:LA:WA:PO:EH", name = "suite 2", position=[2,3,0])
    petco.add_node(node_type = "anchor", node_id = "TI:PS:XD:WA:PO:EH", name = "suite 3", position=[8,3,0])
    petco.add_node(node_type = "anchor", node_id = "TI:PS:XD:WA:PO:EY", name = "bar", position=[5,0,0])

    env.simulation()

    #clean up threads after time
    env.clean_up()
    print("Goodbye")