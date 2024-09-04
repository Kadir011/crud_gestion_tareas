####################
class Task:
    def __init__(self, name, status=False):
        self.name = name 
        self.status = status 

    def mark_as_done(self):
        self.status = True 

    def __str__(self):
        status_str = "Completed" if self.status else "Pending"
        return f"{self.name} - {status_str}"







