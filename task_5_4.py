model = {"TE100-S5":
             {"product Title": "5-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "5x",
              "Forearding Capacity": "1 Gbps",
              "MAC adress entries": "2 k",
              "Enclozure Material": "Plactic"},
         "TE100-S8":
              {"product Title": "9-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "8x",
              "Forearding Capacity": "1.6 Gbps",
              "MAC adress entries": "2 k",
              "Enclozure Material": "Plactic"},
         "TE100-S50g":
             {"product Title": "5-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "5x",
              "Forearding Capacity": "1 Gbps",
              "MAC adress entries": "1 k",
              "Enclozure Material": "Metal Rackmount"},
         "TE100-S80g":
              {"product Title": "9-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "8x",
              "Forearding Capacity": "1.6 Gbps",
              "MAC adress entries": "1 k",
              "Enclozure Material": "Metal Rackmount"},
         "TE100-S16":
             {"product Title": "5-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "5x",
              "Forearding Capacity": "1 Gbps",
              "MAC adress entries": "8 k",
              "Enclozure Material": "Metal Rackmount"},
         "TE100-S24":
              {"product Title": "9-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "8x",
              "Forearding Capacity": "1.6 Gbps",
              "MAC adress entries": "8 k",
              "Enclozure Material": "Metal Rackmount"},
         }

for switch in model.keys():
    if model[switch]['10/100Mbps'] == "5x" and \
            model[switch]["MAC adress entries"] == "1k":
        print(model[switch])