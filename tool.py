import subprocess
import os.path
from config import Config


class Tool:

    JDEPS_VERSION_PARAM = "--version"

    config = Config()

    def is_jdeps_available(self):
        return os.path.exists(self.config.get_path())


    # params should be list!
    def run_jdeps(self, params):
        all_params = [self.config.get_path()]  
        all_params.extend(params)
        return subprocess.run(all_params, capture_output=True, text=True).stdout.strip()    



def main():
    tool = Tool()
    print("Jdeps available?: " + str(tool.is_jdeps_available()))
    print("Checking Jdeps version: " + tool.run_jdeps([tool.JDEPS_VERSION_PARAM]))


if __name__ == "__main__":
    main()
