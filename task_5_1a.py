copmuters = {
    "pc1": {
        "os": "Windows 10",
        "procossor": "ADM Phenom II",
        "ram": "8 Gb",
        "motherboard": "MSI875656",
        "hdd": "1Tb",
    },
    "pc2": {
        "os": "Windows 10",
        "procossor": "ADM Phenom I",
        "ram": "4 Gb",
        "motherboard": "MSI845656",
        "hdd": "512Gb",
    },
    "pc3": {
        "os": "Windows 7",
        "procossor": "ADM Phenom II",
        "ram": "4 Gb",
        "motherboard": "Asus-4565",
        "hdd": "1Tb",
    },
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(copmuters[device][parameter])

