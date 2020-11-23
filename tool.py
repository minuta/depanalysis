import subprocess
import os.path


JDEPS_PATH = '/usr/lib/jvm/java-11-openjdk/bin/jdeps'
JDEPS_VERSION = "11.0.8"


def is_jdeps_available():
    return os.path.exists(JDEPS_PATH)


def run_jdeps(params):
    all_params = [JDEPS_PATH]  
    all_params.extend(params)
    return subprocess.run(all_params, capture_output=True, text=True).stdout.strip()    




def main():
    pass

if __name__ == "__main__":
    main()
