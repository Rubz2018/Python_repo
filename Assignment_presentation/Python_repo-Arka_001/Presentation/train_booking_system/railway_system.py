# railway_system.py

from train import Train

class RailwaySystem:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def show_all_trains(self):
        print("\n📋 Available Trains:")
        for train in self.trains:
            train.display_info()

    def find_train(self, train_no):
        for train in self.trains:
            if train.train_no == train_no:
                return train
        return None
