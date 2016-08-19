#The following implementation of singleton comes from http://www.python.org/dev/peps/pep-0318/#examples
def singleton(cls):
    '''
    Good ol' singleton pattern, if an instance exists, return it
    '''
    instances = {}
    instances_param = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            instances_param[cls] = args
        if len(args) > 0 and instances_param[cls] != args:
            instances[cls] = cls(*args, **kwargs)
            instances_param[cls] = args
        return instances[cls]
    return getinstance