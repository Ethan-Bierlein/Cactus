def cactus_class_method_exception_handle(function):
    """
    This function provides a general wrapper for
    handling errors with the Cactus engine. Example
    usage:
    
        @cactus_class_method_exception_handle
        def my_class_method(self, args):
            code
    """
    def wrapper(self, *args, **kwargs):
        try:
            return function(self, *args, **kwargs)
        except Exception as cactus_game_error:
            with open("cactus_error_log.txt", "w+") as cactus_error_log:
                print("Program has encountered an error. If you believe that this is an engine-related error, please report it at https://github.com/ShearOfDoom/Cactus/issues")
                cactus_error_log.write("Cactus error log")
                cactus_error_log.write("=" * 15)
                cactus_error_log.write("Class Data: " + self.class_data)
                cactus_error_log.write("=" * 15)
                cactus_error_log.write(str(cactus_game_error))
                cactus_error_log.write("=" * 15)
    return wrapper