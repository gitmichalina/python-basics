import sys

global global_counter
global_counter = 0


def main():
    print(f"global_counter: {global_counter}")
    increase_counter()
    print(f"global_counter: {global_counter}")


def increase_counter():
    # global global_counter
    # print(f"global_counter: {global_counter}")
    #     # global_counter += 1
    global_counter = 8
    print(f"global_counter: {global_counter}")

    enclosed_var = 0
    print(f"enclosed_var: {enclosed_var}")

    def inner_func():
        nonlocal enclosed_var
        enclosed_var += 2
        # global global_counter
        # global_counter = 6
        print(f"global_counter inside inner_func: {global_counter}")

    inner_func()
    print(f"enclosed_var: {enclosed_var}")
    print(f"global_counter: {global_counter}")


if __name__ == '__main__':
    main()




    smaller_list = ['ArithmeticError', 'AssertionError', 'AttributeError',
                    'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError',
                    'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
                    'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError',
                    'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
                    'Exception', 'False', 'FileExistsError', 'FileNotFoundError',
                    'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError',
                    'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
                    'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt',
                    'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None',
                    'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
                    'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
                    'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning',
                    'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration',
                    'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError',
                    'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
                    'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
                    'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
                    'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__',
                    '__doc__', '__import__', '__loader__', '__name__', '__package__',
                    '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray',
                    'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex',
                    'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
                    'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset',
                    'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input',
                    'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
                    'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
                    'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
                    'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
                    'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

    print(dir(__builtins__))
    print(__builtins__.__dict__.keys())
    print(dir())



    # for k, v in __builtins__.__dict__.items():
    #     print(k, "is", v)

    # ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError',
    # 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
    # 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning',
    # 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError',
    # 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
    # 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError',
    # 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
    # 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
    # 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning',
    # 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
    # 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning',
    # 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__',
    # '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray',
    # 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir',
    # 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals',
    # 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license',
    # 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print',
    # 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
    # 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

    # built_in_namespace = ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup',
    #                'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError',
    #                'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError',
    #                'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception',
    #                'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
    #                'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
    #                'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt',
    #                'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError',
    #                'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
    #                'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning',
    #                'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError',
    #                'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
    #                'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
    #                'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError',
    #                'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__',
    #                '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool',
    #                'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex',
    #                'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
    #                'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex',
    #                'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map',
    #                'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
    #                'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
    #                'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


