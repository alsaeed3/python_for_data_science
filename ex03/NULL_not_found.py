def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object != object:
        print(f"Cheese: nan {type(object)}")
    elif object == 0 or object is False:
        if isinstance(object, bool):
            print(f"Fake: False {type(object)}")
        elif isinstance(object, int):
            print(f"Zero: 0 {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
