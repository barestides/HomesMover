import re

world_name = '9348781237813432'


# Read homes
def simple_home_reader():
    original_db = open('sources/simplehomes.yml', 'r')
    contents = original_db.read()
    lines = contents.splitlines()
    homes = []
    players = {}
    for i, line in enumerate(lines):
        if(i%6 == 0):
            print(line)


simple_home_reader()