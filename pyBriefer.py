import argparse, json

def brief(obj,item=4,prefix=""):
    if type(obj) == type(dict()):
        if len(obj.keys()) > item:
            key_list = list(obj.keys())[:item]
        else:
            key_list = list(obj.keys())
        print(prefix+"  count[{}]:".format(len(list(obj.keys()))))
        for key in key_list:
            print(prefix+"  - \"{}\" {}".format(key,type(obj[key])))
            value = obj[key]
            brief(value,prefix="    "+prefix)
        if len(obj.keys()) > item:
            print(prefix+"  - ......")
    elif type(obj) == type(list()) or type(obj) == type(set()) :
        obj_list = list(obj)
        if len(obj_list) > item:
            key_list = [n for n in list(obj_list)[:item]]
            end_str = ", ......"
        else:
            key_list = [n for n in obj_list]
            end_str = ""
        if True in [(type(n) == type(dict())) for n in key_list]:
            print(prefix+"  count[{}]:".format(len(obj_list)))
            for unit_i, unit in enumerate(key_list):
                print(prefix+"  - item[{}]".format(unit_i))
                brief(unit,prefix="    "+prefix)
        # if True not in [(type(n) == type(dict())) for n in key_list]:
        else:
            format_list = ["\"{}\"".format(n) for n in key_list]
            print(prefix+"  count[{}]: {}{}".format(len(obj_list),", ".join(format_list),end_str))
    else:
        print(prefix+"  Content: \"{}\" {}".format(obj,type(obj)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser('JSON/Dictionary summary')
    parser.add_argument('-i', '--input', type=str, required = True,
                        help='input JSON')
    args = parser.parse_args()

    print(F"\"{args.input}\"")
    brief(json.load(open(args.input)))
