import os
import traceback
try:
 inputfile = input("PLZ Enter The Input File Path\n")
 inp = open(inputfile, "r+")
 logfile = input("PLZ Enter The Log File Path\n")
 try:
     os.remove(logfile)
 except:
     print("No Log File To Remove")
 else:
     print("Log File Removed")
     log = open(logfile, "a+")
     log.write("{}\t{}\n".format("Path", "Remove Status"))
     log.close()


except:
    print(traceback.print_exc())
for file in inp.readlines():
    try:
      os.remove(file.strip())
      print(f'{file.strip()} Removed Successfully')
      log = open(logfile, "a+")
      log.write("{}\t{}\n".format(file.strip(), "Removed Successfully"))
      log.close()
    except FileNotFoundError:
        print(f'{file.strip()} Not Exists')
        log = open(logfile, "a+")
        log.write("{}\t{}\n".format(file.strip(), "Not Exists"))
        log.close()
    except OSError:
        print(f'{file.strip()} Have Invalid Characters')
        log = open(logfile, "a+")
        log.write("{}\t{}\n".format(file.strip(), "Have Invalid Characters"))
        log.close()
    inp.close()

