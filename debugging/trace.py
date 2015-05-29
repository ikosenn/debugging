

def trace_it(frame, event, arg):
    if event == 'line':
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        print filename, lineno
    return trace_it
