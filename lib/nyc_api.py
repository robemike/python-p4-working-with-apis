import requests
import json

class GetPrograms:

  # Define a function which will send a request to the specified end-point
  def get_programs(self):
    # Assign the endpoint url to the variable URL.
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
    # Create a response object which will display the reponse content obtained after the request.
    response = requests.get(URL)
    # Return the response content.
    return response.content

  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        # Create a list which will store the dictionaries.
        programs_list = []
        # Here we parse the response which is in JSON format/ becomes a dictionary which we can work with.
        programs = json.loads(self.get_programs())

        for program in programs:
            # Append the dictionaries to the list.
            programs_list.append(program["agency"])

        return programs_list

#programs = GetPrograms().get_programs()
#print(programs)

programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
    print(agency)