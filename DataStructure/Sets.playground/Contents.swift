import Foundation

/*
    * Sets uses an Hashtable under the hood to store their values. That's why each single entry in a set is unique
    * Each value of the set are turned into a hash, which can be used to find easily(O(1)) find where an element is in the set.
    *
 
 
 */


//************************************************************************************
var basicSet: Set<Int> = [1,2,3,4,4]
var otherSet: Set<Int> = [19,10,34,3]


// Operation 1 - Insert
basicSet.insert(6)


// Operation 2 - Remove
basicSet.remove(4)


// Operation 3 - Contains
if (basicSet.contains(6)) {
    // Since a set uses a HashTable, looking up "6" is contant time, instead of iterative.
//    print("There is a 6 in the Set")
}

var setUnion = basicSet.union(otherSet)
var setIntersection = basicSet.intersection(otherSet)
var setSymetricDifference = basicSet.symmetricDifference(otherSet)

//print("Union Between set A and set B is \(setUnion)")
//print("Intersection Between set A and set B is \(setIntersection)")
//print("Symetric Difference Between set A and set B is \(setSymetricDifference)")
//************************************************************************************



// Finds elements that both sequence have in commond - similar to .intersection() method of the Set class
func findIntersection(sequenceA: [Int], sequenceB: [Int]) -> [Int] {
    
    
    /*
        Sequence A: 1,2,3,4,5
        Sequence B: 7,1,10,5
     
        seenElements: {
            1: 2
            2: 1
            3: 1
            4: 1
            5: 2
            7: 1
            10: 1
        }
     
        commonElement [1,5] // Only return elements that have been seen more than once
     */
    var commonElements = [Int]()
    var seenElements = [Int: Int]()
    
    // Time Complexity: 0(n) where n is # of elem in the sequence
    sequenceA.forEach { (elem) in
        if(seenElements[elem] != nil) {
            // set it to 1 if never seen before
            seenElements[elem] = 1
        } else {
            // increase by 1 if seen befoe
            seenElements[elem]! += 1
        }
    }
    
    // Time Complexity: 0(n) where n is # of elem in the sequence
    sequenceB.forEach { (elem) in
        if(seenElements[elem] != nil) {
            // set it to 1 if never seen before
            seenElements[elem] = 1
        } else {
            // increase by 1 if seen befoe
            seenElements[elem]! += 1
        }
    }
    
    // Time Complexity: 0(n) where n is # of elem in the sequence
    seenElements.forEach { (key, value) in
        if(value > 1) {
            commonElements.append(value)
        }
    }
    
    return commonElements
}


let seqA = [1,2,3,4]
let seqB = [6,7,1]
let result = findIntersection(sequenceA: seqA, sequenceB: seqB)
print(result)


func findSymetricDifference() {
    
}




//************************************************************************************



// In oder to use a "set of movies", the struct needs to conform to the "Hashable protocol"
struct Movie: Hashable {
    var name: String
    var year: Int
    var rating: Int
    
    
    init(name: String, year: Int, rating: Int) {
        self.name = name
        self.year = year
        self.rating = rating
    }
    
    init(name: String) {
        self.name = name
        self.year = 0
        self.rating = 0
    }
    
    static func == (lhs: Movie, rhs: Movie) -> Bool {
        return lhs.name == rhs.name
    }
    
    // This method is part of the Hashable method that uses the "name" property as the way to set up the HashTable mechanism
    func hash(into hasher: inout Hasher) {
        hasher.combine(name)
    }
}

let moviesSet:Set = [
    Movie(name: "Rocky", year: 1976, rating: 5),
    Movie(name: "The Matrix", year: 1999, rating: 10),
    Movie(name: "Lord Of The Rings", year: 2001, rating: 8),
    Movie(name: "The Secret Life Of Walter Mitty", year: 2013, rating: 7),
    Movie(name: "Deadpool", year: 2016, rating: 3)
]

if moviesSet.contains(Movie(name: "Rocky")) {
    print("Yes! Rocky is a favorite.")
}


//************************************************************************************

