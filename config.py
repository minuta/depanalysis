import json

class Config:

    def __init__(self):
        self.settings = self.read_path_from_config()

    def read_path_from_config(self):
        with open('config.json') as f:
            settings = json.load(f)
        return settings

    def get_path(self):
        return self.settings["JDEPS_PATH"]

if __name__ == "__main__":
    cfg = Config()
    print(cfg.read_path_from_config())
