import json
from pprint import pprint
with open('template.json') as f:
    file_content = f.read()
    template = json.loads(file_content)

# Вывод всехданных
pprint(template)
model = template
print("------------------------------------------------------")
# Вывод по условию
for switch in model.keys():
    if model[switch]['10/100Mbps'] == "5x" and \
            model[switch]["MAC adress entries"] == "1 k":
        pprint(model[switch])