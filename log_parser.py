

import re

file_name = '/Users/cchavez/dev/PythonFundamentals.Labs.RSVPAgentProcessingLogParser/data/rsvp_agent_log.dat'
print("WARNINGS:")
with open(file_name, "r+") as data_file:
   for lines in data_file:
      match = re.search("WARNING", lines)
      if match == None:
         pass
      else:
         print(str(lines[0:14]) + " -- " + str(re.split(lines[45:]))
