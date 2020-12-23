from .schemas import Counter

from sqlalchemy.orm import Session

class CounterStorage:
    def __init__(self):
        self.counters = []

    def create_or_get_counter(self, name, createmode=True):
        try:
            counter = next(filter(lambda c: c.name == name, self.counters))
        except StopIteration:
            if createmode:
                counter = Counter(name=name, count=0)
                self.counters.append(counter)
            else:
                counter = None
        return counter
    
#    def create_counter(self, db: Session, counter: Counter):
#        db.add(counter)
#        db.commit()
#        db.refresh(counter)
#        return counter

    
    def delete_counter_by_name(self, name):
        if name in self.counters:
            self.counters.pop(name)
        

    def increment_by_name(self, name):
        counter = self.create_or_get_counter(name)
        counter.count += 1
        return counter

    def decreament_by_name(self, name):
        counter = self.create_or_get_counter(name)
        counter.count -= 1
        return counter
    
    def reset_by_name(self, name):
        counter = self.create_or_get_counter(name)
        counter.count = 0
        return counter