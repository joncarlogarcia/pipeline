
class Pipeline:

    def __init__(self):
        self.tasks = []


    # TODO: Implement task function
    def task(self, function, depends_on=None):
        names = [name.__name__ for name in self.tasks]
        
        if depends_on is None:
            self.tasks.append(function)
            
        if depends_on == 'first_task' and 'first_task' in names:
            self.tasks.append(function)

        elif depends_on == 'second_task' and 'second_task' in names:
            self.tasks.append(function)

        else:
            pass

            
    # TODO: Implement run function
    def run(self, value):
        inputValue = self.tasks[0](value)

        for func in self.tasks[1:]:
            inputValue = func(inputValue)

        return inputValue


pipeline = Pipeline()

@pipeline.task
def first_task(x):
    return x - 1

def second_task(x):
    return x ** 2
pipeline.task(second_task, depends_on='first_task')

def last_task(x):
    return x + 4
pipeline.task(last_task, depends_on='second_task')

print pipeline.run(50)
