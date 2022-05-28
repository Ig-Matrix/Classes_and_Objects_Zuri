from typing import List
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name:str, age:int, tracks:List[str], score:float):
       self.name=name
       self.age=age
       self.tracks=tracks
       self.score=score

    def  change_name(self, name):
        self.name=str(name)
    
    def change_age(self, age):
        self.age=int(age)

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34.8)
Bob.add_track("UI/UX")
Bob.get_score()


