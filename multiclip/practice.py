import sys
import clipboard
import json

SAVED_DATA = 'test.json'

def save_data(filepatah, data):
    with open(filepatah, 'w') as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input("Enter a key to save under: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print(f"Data copied under {key}")
    elif command == 'load':
        key = input ( "Enter a key to load from: ")
        if key in data:
            clipboard.copy(data[key])
            print(f"data loaded under {key}")
        else:
            print("Key doesn't exist.")
    elif command == 'list':
        print("Clipboard items: ", data)
    else:
        print("Enter valid command. (save/load/list)")
else:
    print("Enter exactly one command.")
