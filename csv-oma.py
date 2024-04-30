with open("grades.csv") as new_file:
    for line in new_file:
        # Poistetaan rivinvaihdot
        line = line.replace("\n", "")
        # Jaetaan tietokentät taulukkoon
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]
        print("Name:", name)
        print("Grades:", grades)