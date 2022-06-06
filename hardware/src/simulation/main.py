# author: Marcin Kierebinski
import numpy
import time
import datetime
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

    def setupTables(self):
        # Create company
        query = 'INSERT INTO Companies (id, name, payment, phone_number, street_address, city, state, country, postal_code, company_code, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = ('99806','Hirthe Group', '3015-063767-6726', '1-675-246-4169', '2508 Herman Forks', 'Port Osbaldo', 'Nevada', 'Berkshire', '69917-3353', '2886926585', datetime.datetime.now())
        self.server.insert_record(query,values)

        # Create venue organizer profile
        query = 'INSERT INTO Customers (id, first_name, last_name, email, username, password, company_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        values = ('28685','Christop', 'Bruen', 'cBruen@gmail.com', 'cBruen', 'sed', '99806', datetime.datetime.now())
        self.server.insert_record(query,values)

        # Create event
        query = 'INSERT INTO Events (id, name, datetime_start, datetime_end, street_address, city, state, country, postal_code, category, customer_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = ('4296','Ebert Inc', 'Mon Apr 24 2023 03:00:23 GMT-0700 (Pacific Daylight Time)', 'Mon Apr 24 2023 09:00:23 GMT-0700 (Pacific Daylight Time)', '8916 Trever Grove', 'North Tiffany', 'Montana', 'Berkshire', '50967-6948', 'Football', '28685', datetime.datetime.now())
        self.server.insert_record(query,values)

        # Create suites
        query = 'INSERT INTO Suites (id, name, number_active, event_id, created_at) VALUES (%s, %s, %s, %s, %s)'
        values = [('31764', 'suite #1', '0', '4296', datetime.datetime.now()),
                    ('22477', 'suite #2', '0', '4296', datetime.datetime.now()),
                    ('3856', 'suite #3', '0', '4296', datetime.datetime.now()),
                    ('3075', 'suite #4', '0', '4296', datetime.datetime.now()),
                ]
        self.server.insert_records(query,values)

        # Create Services
        query = 'INSERT INTO Services (id, name, event_id, created_at) VALUES (%s, %s, %s, %s)'
        values = [('8646', 'Snack Vendor', '4296', datetime.datetime.now()),
                    ('19332', 'Bar', '4296', datetime.datetime.now()),
                    ('27462', 'Kitchen', '4296', datetime.datetime.now()),
                ]
        self.server.insert_records(query,values)

        # Create Employees
        query = 'INSERT INTO Employees (id, first_name, last_name, badge_id, service_id, created_at) VALUES (%s, %s, %s, %s)'
        values = [('8646','Lavon', 'Jacobi', '101436307', '8646', datetime.datetime.now()),
                    ('19332','Lennie', 'Hamill', '362623547', '19332', datetime.datetime.now()),
                    ('27462','Fiona', 'Lynch', '2570210177', '27462', datetime.datetime.now()),
                ]
        self.server.insert_records(query,values)

        # Create Services products
        query = 'INSERT INTO Products (id, name, price, service_id, created_at) VALUES (%s, %s, %s, %s, %s)'
        values = [('1908', 'pretzels', '12.00', '8646', datetime.datetime.now()),
                    ('5043', 'chocolate', '5.00', '8646', datetime.datetime.now()),
                    ('505', 'chips', '12.00', '8646', datetime.datetime.now()),

                    ('22457', 'beer', '10.00', '19332', datetime.datetime.now()),
                    ('3680', 'drink', '20.00', '19332', datetime.datetime.now()),
                    ('12044', 'shot', '10.00', '19332', datetime.datetime.now()),

                    ('7700', 'chicken', '15.00', '27462', datetime.datetime.now()),
                    ('29197', 'pizza', '25.00', '27462', datetime.datetime.now()),
                    ('19783', 'burrito', '14.00', '27462', datetime.datetime.now()),
                ]
        self.server.insert_records(query,values)

        # Create Users
        # query = 'INSERT INTO Users (id, first_name, last_name, phone_number, email, username, password, payment, datetime_check_in, datetime_check_out, isOwner, survey_id, suite_id, rfid_id, mac_address, created_at) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # values = [('2081','Nick', 'K', '(238) 696-4692 x6979', 'nk@red.com', 'red', 'red', '6709034532786922','None', 'None', 'true', 'None', 'None', 'None', 'None', datetime.datetime.now()),
        #             ('9477','Karen', 'Z', '632-510-6854 x8042', 'kz@red.com', 'pink', 'pink', '3529-0147-4449-3664','None', 'None', 'false', 'None', 'None', 'None', 'None', datetime.datetime.now()),
        #             ('5766','Marcin', 'K', '(547) 806-4895', 'mk@red.com', 'black', 'black', '5018910943422954649','None', 'None', 'false', 'None', 'None', 'None', 'None', datetime.datetime.now()),
        #             ('22617','Raymond', 'U', '821-897-6202', 'ru@red.com', 'blue', 'blue', '3650-988381-0933','None', 'None', 'false', 'None', 'None', 'None', 'None', datetime.datetime.now()),
        #             ('12491','Rusul', 'A', '642-965-3323', 'ra@red.com', 'orange', 'orange', '677178312218474740','None', 'None', 'false', 'None', 'None', 'None', 'None', datetime.datetime.now()),
        #         ]
        # self.server.insert_records(query,values)

    def simulation(self):
        #check people in
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LG:LA:PO:EH",name="Nick")
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LA:LA:PO:EH",name="Karen",color='pink')
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:LG:LA:PO:EF",name="Marcin",color='black')
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TA:PS:LG:LA:PO:EF",name="Raymond",color='blue')
        self.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].check_in("TI:PS:ER:LA:PO:EF",name="Rusul",color='orange')

        # Create Users
        query = 'INSERT INTO Users (id, first_name, last_name, phone_number, email, username, password, payment, datetime_check_in, datetime_check_out, isOwner, survey_id, suite_id, rfid_id, mac_address, created_at) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = [('2081','Nick', 'K', '(238) 696-4692 x6979', 'nk@red.com', 'red', 'red', '6709034532786922','None', 'None', 'true', 'None', 'None', '[45, 227, 129, 56]', 'TI:PS:LG:LA:PO:EH', datetime.datetime.now()),
                    ('9477','Karen', 'Z', '632-510-6854 x8042', 'kz@red.com', 'pink', 'pink', '3529-0147-4449-3664','None', 'None', 'false', 'None', 'None', '[45, 27, 129, 56]', 'TI:PS:LA:LA:PO:EH', datetime.datetime.now()),
                    ('5766','Marcin', 'K', '(547) 806-4895', 'mk@red.com', 'black', 'black', '5018910943422954649','None', 'None', 'false', 'None', 'None', '[99, 197, 79, 28]', 'TI:PS:LG:LA:PO:EF', datetime.datetime.now()),
                    ('22617','Raymond', 'U', '821-897-6202', 'ru@red.com', 'blue', 'blue', '3650-988381-0933','None', 'None', 'false', 'None', 'None', '[45, 27, 19, 56]', 'TA:PS:LG:LA:PO:EF', datetime.datetime.now()),
                    ('12491','Rusul', 'A', '642-965-3323', 'ra@red.com', 'orange', 'orange', '677178312218474740','None', 'None', 'false', 'None', 'None', '[45, 27, 129, 59]', 'TI:PS:ER:LA:PO:EF', datetime.datetime.now()),
                ]
        self.server.insert_records(query,values)
        
        # #simulating movements
        # trace = 3
        simulation_time = 10
        for timestep in range(simulation_time):
            pos_1 = petco.node_dict['tag']['TI:PS:LG:LA:PO:EH'].sim_update_position()
            pos_2 = petco.node_dict['tag']['TI:PS:LA:LA:PO:EH'].sim_update_position()
            pos_3 = petco.node_dict['tag']['TI:PS:LG:LA:PO:EF'].sim_update_position()
            pos_4 = petco.node_dict['tag']['TA:PS:LG:LA:PO:EF'].sim_update_position()
            pos_5 = petco.node_dict['tag']['TI:PS:ER:LA:PO:EF'].sim_update_position()
            #self.position: np.array of 3 elements
            # x y z

            # insert LocationLogs records
            query = 'INSERT INTO LocationLogs (location_log, mac_address, created_at) VALUES (%s, %s, %s)'
            # uploading data to database should be done by numpy array => list
                # receiving from database should be done by list => numpy array
            values = [(f'{pos_1.tolist()}', 'TI:PS:LG:LA:PO:EH', datetime.datetime.now()),
                        (f'{pos_2.tolist()}', 'TI:PS:LA:LA:PO:EH', datetime.datetime.now()),
                        (f'{pos_3.tolist()}', 'TI:PS:LG:LA:PO:EF', datetime.datetime.now()),
                        (f'{pos_4.tolist()}', 'TA:PS:LG:LA:PO:EF', datetime.datetime.now()),
                        (f'{pos_5.tolist()}', 'TI:PS:ER:LA:PO:EF', datetime.datetime.now()),
                    ]
            self.server.insert_records(query,values)
            
            trans_1 = None
            trans_2 = None
            trans_3 = None
            values = []
            if petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].get_updates():
                trans_1 = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].get_most_recent_transaction()
                # rfid Node.id => petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].self.id
                #suites are unassigned and datapoints move everywehre soooooo make all attendees assigned to one suite for simplicity
                if trans_1 is not None: values.append((datetime.datetime.now(), '???', '???', datetime.datetime.now()))

            if petco.node_dict['gateway']['TI:AA:LA:LA:PO:EG'].get_updates():
                trans_2 = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EG'].get_most_recent_transaction()
                if trans_2 is not None: values.append((datetime.datetime.now(), '???', '???', datetime.datetime.now()))

            if petco.node_dict['gateway']['TI:AA:LA:LA:PO:EE'].get_updates():
                trans_3 = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EE'].get_most_recent_transaction()
                if trans_3 is not None: values.append((datetime.datetime.now(), '???', '???', datetime.datetime.now()))

            # insert Transactions records
            if values:
                query = 'INSERT INTO Transactions (timestamp, product_id, rfid_id, created_at) VALUES (%s, %s, %s, %s)'
                self.server.insert_records(query,values)

            # position = petco.node_dict['tag']['TI:PS:LA:LA:PO:EH'].sim_update_position()
            # position = petco.node_dict['tag']['TI:PS:LG:LA:PO:EH'].sim_update_position()
            # position = petco.node_dict['tag']['TI:PS:LG:LA:PO:EF'].sim_update_position()
            # position = petco.node_dict['tag']['TA:PS:LG:LA:PO:EF'].sim_update_position()
            # position = petco.node_dict['tag']['TI:PS:ER:LA:PO:EF'].sim_update_position()
            # transaction = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EH'].get_updates()
            # transaction = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EG'].get_updates()
            # transaction = petco.node_dict['gateway']['TI:AA:LA:LA:PO:EE'].get_updates()

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
    
    # setup database tables for simulation data
    env.setupTables()

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