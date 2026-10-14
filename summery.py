with open("demo_logs.log",'r') as file :
    for line in file:
        if "ERROR" in line:
            with open("error_logs.log",'a') as error_file:
                error_file.write(line)
        elif "WARNING" in line:
            with open("warning_logs.log",'a') as warning_file:
                warning_file.write(line)
        elif "INFO" in line:
            with open("info_logs.log",'a') as info_file:
                info_file.write(line)
        elif "DEBUG" in line:
            with open("debug_logs.log",'a') as debug_file:
                debug_file.write(line)
