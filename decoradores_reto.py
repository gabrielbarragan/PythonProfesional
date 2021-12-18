from datetime import datetime

def logger(file_log):
    """ Decorator to capture the execution time of a function."""
    def decorator_log(func):

        def wrapper(*args, **kwargs):
            """Writes to a file the executed function and the time at which it was executed"""
            with open(file_log, 'a') as opened_file:
                time_log = datetime.now()
                func_output = func.__name__
                output = func(*args, **kwargs)
                opened_file.write(f'{time_log}: {func_output}\n')
                return output

        return wrapper
    return decorator_log
    
@logger('logger.log')
def suma(a,b):
    return a + b

def run():
    print(suma(1,5))

if '__main__' == __name__:
    run()