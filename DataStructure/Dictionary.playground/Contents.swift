import Foundation

var studentScores: [String: Int] = ["Medi": 80, "Robert": 97, "Trever": 70]
print(studentScores)

// Adding element into a dictionary
studentScores["Giselle"] = 85
print(studentScores)


// Removing an element from a deictionary
studentScores.removeValue(forKey: "Giselle")
print(studentScores)

studentScores["Medi"] = nil
print(studentScores)




