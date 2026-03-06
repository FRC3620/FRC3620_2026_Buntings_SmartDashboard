import json
import logging
import os

def main():
    output = []

    tabs_in_files = {}

    with open('wanted.txt', 'r') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('#'):
                continue
            if len(line) == 0:
                continue

            file, tabname = line.split("/")
            filename = file + ".json"

            tabs_in_file = tabs_in_files.get(file)
            if tabs_in_file is None:
                with open(filename, 'r') as json_file:
                    j = json.load(json_file)
                    tabs_in_file = tabs_in_files[file] = { }
                    for t in j.get('tabs'):
                        name = t['name']
                        tabs_in_file[name] = t

            pane = tabs_in_file.get(tabname)
            if pane is None:
                logging.error("Can't find {}", line)
            else:
                output.append(pane)

        outdata = {
            'version': 1.0,
            'grid_size': 128,
            'tabs': output,
        }

    with open('2026_combined.json', 'w') as outfile:
        json.dump(outdata, outfile, sort_keys=True, indent=1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

