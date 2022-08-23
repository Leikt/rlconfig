class GloballyAccessible(type):
    _instances = {}

    def __call__(cls, name, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = {}
        if name not in cls._instances[cls]:
            cls._instances[cls][name] = super(GloballyAccessible, cls).__call__(*args, **kwargs)
        return cls._instances[cls][name]

    def __clear__(cls):
        if cls in cls._instances:
            del cls._instances[cls]
