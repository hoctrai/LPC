from main import BridgingDatabaseToAlgorithmStrategy
from main.Algorithm import parrot_r

class Algorithm():
    bridge = object()

    db_table = []
    # list_data =[]
    HS = []
    TS = []
    rs_1 = []
    def __init__(self):
        self.bridge = BridgingDatabaseToAlgorithmStrategy.Main_Bridge()

        self.set_data()

        self.HS = self.set_sub_data('HS')
        self.TS = self.set_sub_data('TS')
        self.rs_1 = self.set_sub_data('rs_1')

        print()

    def set_data(self):
        print ()
        self.db_table = self.bridge.get_table()

    def set_sub_data(self,str_type):
        list_data = [k for k in [h for h in self.db_table if(h[1] == str_type)] if(k.is_integer())]
        return list_data

    def run(self):
        algorithm = input("chose algorithm: ")
        if algorithm == 1:
            par_r = parrot_r.parrot_r(self.HS, self.TS, self.rs_1 )




run = Algorithm()
run.run()