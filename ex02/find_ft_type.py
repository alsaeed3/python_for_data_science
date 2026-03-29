def all_thing_is_obj(object: any) -> int:
    objType = {list: "List",
               tuple: "Tuple",
               set: "Set",
               dict: "Dict",
               str: f"{object} is in the kitchen"}

    if type(object) not in objType:
        print("Type not found")
        return 42

    print(f"{objType.get(type(object))} : {type(object)}")
    return 42
