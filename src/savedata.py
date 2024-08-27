import os, json


class Savedata:
    def __init__(self):
        self.load_savedata()
    
    def load_savedata(self):
        try:
            with open("savedata.json", "r") as f:
                try:
                    self.savedata = json.load(f)
                except json.decoder.JSONDecodeError:
                    self.savedate = {"highscore": 0, "runs": 0, "level": 1, "currency": {"coins" : 0, "gems" : 0}}
        except FileNotFoundError:
            self.savedata = {"highscore": 0, "runs": 0, "level": 1, "currency": {"coins" : 0, "gems" : 0}}
            with open("savedata.json", "w") as f:
                json.dump(self.savedata, f)