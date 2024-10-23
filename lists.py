trainees = ["John", [2, ["James", "Mary"]]]

print(trainees[1][0])  # Display 2
print(trainees[1][1][0])  # Output James

trainees.append(56)
print(trainees)  # Add 56 at the end

trainees[1][1].insert(1, "Mike")
print(trainees)  # Add Mike between James and Mary

trainees[1][0] = 86
print(trainees)  # Change 2 to 86

trainees.remove("John")
trainees[1][1].remove("Mary")
print(trainees)  # Remove John and Mary

print(len(trainees))  # Determine the length of the list



