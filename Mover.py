import re


# Read homes
def simple_home_reader():
    original_db = open('sources/simplehomes.yml', 'r')
    contents = original_db.read()
    lines = contents.splitlines()
    homes = []
    for i, line in enumerate(lines):
        if not line.startswith(' ') and not line.endswith('{}'):
            player = line[:-1]
            default_home = True
            if re.search('^  \S.*', lines[i + 1]):
                name = 'null'
                if not re.search('^  default:$', lines[i + 1]):
                    default_home = False
                    name = lines[i + 1][2:-1]
                world = lines[i + 2][11:]
                x_coord = lines[i + 3][7:] + '.0'
                y_coord = lines[i + 4][7:] + '.0'
                z_coord = lines[i + 5][7:] + '.0'
                homes.append({'player': player, 'world': world, 'x': x_coord, 'y': y_coord, 'z': z_coord,
                              'default_home': default_home, 'name': name})
                if len(lines) - i > 6:
                    if re.search('^  \S.*', lines[i + 6]):
                        default_home = True
                        name = 'null'
                        if not re.search('^  default:$', lines[i + 6]):
                            default_home = False
                            name = lines[i + 6][2:-1]
                        world = lines[i + 7][11:]
                        x_coord = lines[i + 8][7:] + '.0'
                        y_coord = lines[i + 9][7:] + '.0'
                        z_coord = lines[i + 10][7:] + '.0'
                        homes.append({'player': player, 'world': world, 'x': x_coord, 'y': y_coord, 'z': z_coord,
                                      'default_home': default_home, 'name': name})
    create_hsp_output(homes)
    for home in homes:
        print(home)


def create_hsp_output(homes_list_of_tuples):
    hsp_output = open('output/hsp_output.yml', 'a+')
    hsp_output.write('homes:')
    for i, sh_home in enumerate(homes_list_of_tuples):
        home = '\n  \'' + str(i+1) + '\':\n    ==: Home\n    id: ' + str(
            i+1) + '\n    lastModified: 1458267847321\n    dateCreated: 1458265677106\n    world: ' + sh_home[
                   'world'] + '\n    x: ' + sh_home['x'] + '\n    y: ' + sh_home['y'] + '\n    z: ' + sh_home[
                   'z'] + '\n    pitch: 11.550003\n    yaw: -200.25002\n    name: ' + sh_home[
                   'name'] + '\n    player_name: ' + sh_home['player'] + '\n    updatedBy: ' + sh_home[
                   'player'] + '\n    bedHome: false\n    defaultHome: ' + str(sh_home['default_home']).lower()
        hsp_output.write(home)
    hsp_output.close()

simple_home_reader()
