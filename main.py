from typing import List
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name:str, age:int, tracks:List[str], score:float):
       self.name=name
       self.age=age
       self.tracks=tracks
       self.score=score

    def  change_name(self, name):
        self.name=name
    
    def change_age(self, age:int):
        self.age=age

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name(str("Peter"))
Bob.change_age(int(34))
Bob.add_track(str("UI/UX"))
Bob.get_score()
