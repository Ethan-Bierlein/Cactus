from contextlib import redirect_stdout
from traceback import format_exc
from pprint import pformat
from sys import exit, maxsize
from os import path
from time import strftime
import platform

def _cactus_class_method_exception_handle(function):
    """
    This function provides a general wrapper for
    handling errors with the Cactus engine. Example
    usage:
    
        @_cactus_class_method_exception_handle
        def my_class_method(self, args):
            code
    """
    def wrapper(self, *args, **kwargs):
        try:
            return function(self, *args, **kwargs)
        except Exception as cactus_game_error:
            date_string = strftime("%H_%M_%S_%b_%d_%y")
            
            print("\n" + "=" * 50 + "\n")
            print("Something wrong internally happened (not your fault!). This may be an issue with the game itself, or the") 
            print("underlying components. To help fix this issue, please contact the developers of the game with the error report.") 
            print("")
            print("In your error report, please include the file:")
            print(path.abspath("cactus_error_log_" + date_string +".txt"))
            print("\n" + "=" * 45 + "\n")
            
            with open("cactus_error_log_" + date_string +".txt", "w+") as cactus_error_log:
                with redirect_stdout(cactus_error_log):
                    print("\n" + "=" * 45 + "\n")
                    print("CACTUS GAME ENGINE ERROR REPORT")
                    print("")
                    print("If you think this error is engine-related,")
                    print("please report it to:")
                    print("https://github.com/ShearOfDoom/Cactus/issues/")
                    print("\n" + "=" * 45 + "\n")
                    print("Date/Time: {0}".format(strftime("%c")))
                    print("Operating System: {0}".format(platform.platform()))
                    print("Processor: {0}".format(platform.processor()))
                    print("System [not Python itself] 32 or 64 bit: {0}".format(platform.machine()))
                    print("Is 64-bit Python?: {0}".format(maxsize > 2**32))
                    print("Python: {0} {1} {2} {3}".format(platform.python_implementation(), platform.python_build()[0], platform.python_build()[1], platform.python_compiler()))
                    print("\n" + "=" * 45 + "\n")
                    print("CLASS DATA:", pformat(self.class_data, indent = 2))
                    print("\n" + "=" * 45 + "\n")
                    print("STACK TRACE:", format_exc())
                    print("=" * 45 + "\n")
                    exit(0)
    return wrapper
