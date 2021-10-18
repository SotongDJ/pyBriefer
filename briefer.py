def brief(obj,item=4,prefix=""):
    if type(obj) == type(dict()):
        if len(obj.keys()) > item:
            key_list = list(obj.keys())[:item]
        else:
            key_list = list(obj.keys())
        print(prefix+"  Count[{}]:".format(len(list(obj.keys()))))
        for key in key_list:
            print(prefix+"  - \"{}\" {}".format(key,type(obj[key])))
            value = obj[key]
            brief(value,prefix="    "+prefix)
        if len(obj.keys()) > item:
            print(prefix+"  - ......")
    elif type(obj) == type(list()) or type(obj) == type(set()) :
        obj_list = list(obj)
        if len(obj_list) > item:
            key_list = ", ".join(["\"{}\"".format(n) for n in list(obj_list)[:item]])
            end_str = ", ......"
        else:
            key_list = ", ".join(["\"{}\"".format(n) for n in obj_list])
            end_str = ""
        print(prefix+"  Count[{}]: {}{}".format(len(obj_list),key_list,end_str))
    else:
        print(prefix+"  Content: \"{}\" {}".format(obj,type(obj)))
