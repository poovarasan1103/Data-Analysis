import pandas as pd

data = {
    "ID": list(range(1, 20)),
    
    "Name": [
        "Arun", "Poovi", "Karthi", "Akash", "Maha", "Kesavan", "Rio",
        "Gowtham", "Mani", "John", "Rishi", "Vicky", "Boopoo",
        "Kavi", "Vino", "Hari", "Deva", "Divah", "Dhaksh"
    ],
    
    "Age": [
        25, 20, 28, 23, 27, 29, 21, 22, 29, 30,
        32, 35, 26, 27, 22, 29, 27, 26, 33
    ],
    
    "City": [
        "Coimbatore", "Perambalur", "Trichy", "Kanchipuram", "Vellore",
        "Chennai", "Trichy", "Cuddalore", "Coimbatore", "Trichy",
        "Vellore", "Pblore", "APM", "KPM", "Chennai",
        "Coimbatore", "Pblore", "Kumai", "Ooty"
    ],
    
    "Monthly Salary": [
        25000, 95000, 35000, 20000, 15000, 20000, 23000,
        35000, 35000, 25000, 27000, 16000, 47000,
        15000, 8000, 7000, 5000, 10000, 25000
    ]
}

df = pd.DataFrame(data)

print(df)
