import re

file_name = '/Users/cchavez/dev/PythonFundamentals.Labs.RSVPAgentProcessingLogParser/data/rsvp_agent_log.dat'

print("WARNINGS:")

with open(file_name, "r+") as data_file:
   for line in data_file:
      match = re.search("WARNING", line)
      if match is None:
         pass
      else:
         print(str(line[0:14]) + " -- " + str(line[45:]))
