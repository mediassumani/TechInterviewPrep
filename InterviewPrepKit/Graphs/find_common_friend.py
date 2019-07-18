'''
Find the common friend between two people in a Social Network
'''

from collections import deque

def find_common_friend(graph, from_person, to_person):
    
    people_queue = deque([from_person])
    visited_friends = set()
    
    while len(people_queue) > 0:

        curr_person = people_queue.popleft()
        visited_friends.add(curr_person)
        friends = set(graph[curr_person]).difference(visited_friends)

        for friend in friends:
            if friend == to_person:
                return curr_person
            if friend not in visited_friends:
                people_queue.append(friend)
    return None

def main():

    # Define our graph using an adjencey list
    graph = {}

    # Add the edges between the vertices
    graph['Medi'] = ['Mace', 'Sarin']
    graph['Mace'] = ['Medi']
    graph['Sarin'] = ['Medi', 'Rinni', "Cenz", "Max"]
    graph['Rinni'] = ['Sarin', "Cenz"]
    graph['Cenz'] = ['Sarin', 'Max', "Rinni"]
    graph['Rob'] = []
    graph['Max'] = ["Cenz", "Sarin"]
    
    print(find_common_friend(graph, "Mace", "Max"))

if __name__ == "__main__":
    main()