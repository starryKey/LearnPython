import json

data = {"name":"John","age":18}

with open("test.json", "w") as file:
    json.dump(data, file)

with open("test.json", "r") as f:
    d = json.load(f)
    print(d)

    