def validate_appointment(data: dict):

    list_keys = ['title', 'description', 'where', 'from', 'to', 'repeat', 'repeat_interval',
                 'repeat_times', 'repeated', 'alert', 'alert_moments', 'attachments',
                 'in_trash', 'moved_to_trash']
    list_values = ['str', 'str', 'str', 'int', 'int', 'bool', 'int',
                   'int', 'int', 'bool', 'list_int', 'list_str', 'bool',
                   'int']
    
    n = 0

    for key in data:
        if key != list_keys[n]:
            return False
        elif list_values[n] == 'str':
            isinstance(d[key], str)
            if False:
                break
        elif list_values[n] == 'int':
            isinstance(d[key], int)
            if False:
                break
        elif list_values[n] == 'bool':
            isinstance(d[key], bool)
            if False:
                break
        elif list_values[n] == 'list_int' or 'list_str':
            isinstance(d[key], list)
            if False:
                break
            if list_values[n] == 'list_int':
                
            
            
            
        n = n + 1
        
    

