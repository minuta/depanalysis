import json

class Config:

    CONFIG_FILE_NAME = 'config.json'

    def __init__(self):
        self.settings = self.read_path_from_config()


    def read_path_from_config(self):
        config_data = None
        try:
            with open(self.CONFIG_FILE_NAME) as f:
                config_data = json.load(f)
        except Exception as ex:
            print('ERROR: could not read the config file: {0}'.format(ex))
        return config_data

    def get_path(self):
        return self.settings["JDEPS_PATH"]

    def get_all_config_data(self):
        return self.settings

if __name__ == "__main__":
    cfg = Config()
    print(cfg.get_all_config_data())