class Node():
    def __init__(self, person, parent, movie):
        self.person = person
        self.parent = parent
        self.movie = movie

    def get_person(self):
        return self.person
    
    def get_parent(self):
        return self.parent
    
    def get_movie(self):
        return self.movie


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_person(self, person):
        return any(node.person == person for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
