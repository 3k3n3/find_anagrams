class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

        print('The student\'s name is %s, aged %d years, enrolled in %s with score %.2f.' %(name, age, tracks[1], score))

    def change_name(self, name):
        self.name = name
        print('Student name is' ,name)
        

    def change_age(self, age):
        self.age = age
        print('Student age is' ,age)

    def add_track(self, tracks):
        self.add_track = tracks
        print('Student enrolled in' ,tracks)

    def get_score(self):
        #no new argument is given so the class score is inherited
        print('Student score is' ,self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()