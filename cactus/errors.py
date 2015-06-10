from contextlib import redirect_stdout
from traceback import format_exc
from pprint import pformat
from sys import exit

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
            print("Program has encountered an error. If you believe that this is")
            print("engine-related, please report it to https://github.com/ShearOfDoom/Cactus/issues/")
            print("To find full error stacktrace and details, see cactus_error_log.txt.")
            with open("cactus_error_log.txt", "w+") as cactus_error_log:
                with redirect_stdout(cactus_error_log):
                    print("ERROR")
                    print("\n" + "=" * 45 + "\n")
                    print("CLASS DATA:", pformat(self.class_data, indent=2))
                    print("\n" + "=" * 45 + "\n")
                    print("STACK TRACE:", format_exc())
                    print("=" * 45 + "\n")
                    exit(0)
    return wrapper