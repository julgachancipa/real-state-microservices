class Singleton(type):
    """
    Metaclass implementation of the Singleton pattern
    Taken from https://stackoverflow.com/q/6760685
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
