#!/usr/bin/env python
# student.py
from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Initialize self.knowledge as an empty list

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)  # Add new_knowledge to the knowledge list


 