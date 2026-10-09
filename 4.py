students= {
    101: {"Name" : "Aditi", "Scores":[20, 20, 25]},
    102: {"Name" : "Rahul", "Scores":[15, 18, 22]},
    103: {"Name" : "Jay", "Scores":[12, 16, 20]},
    104: {"Name" : "Aman", "Scores":[10, 14, 18]},
    105: {"Name" : "Riya", "Scores":[8, 12, 16]}
    
}

for sid, details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    details ["Average"] = avg
    details ["Passed"] = avg >= 30 

    print("Students who passed :")
    for sid, details in students.items():
        if details["Passed"]:
            print(details["Name"])