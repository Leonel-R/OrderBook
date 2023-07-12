class Task:
    ids = list(range(1,1001))
    
    def __init__(self, description: str, programmer: str,workload: int) -> None:
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.completed_check = "NOT FINISHED"
        self.id = None
        if self.id not in Task.ids:
            self.id = Task.ids.pop(0)
            
    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.completed_check}"
    
    def is_finished(self):
        if self.completed_check == "NOT FINISHED":
            return False
        return True
    
    def mark_finished(self):
        self.completed_check = "FINISHED"

class OrderBook():
    
    def __init__(self) -> None:
        self.tasks = []
    
    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description,programmer,workload)
        self.tasks.append(task)
    
    def all_orders(self):
        return self.tasks
    
    def programmers(self):
        programmers = [task.programmer for task in self.tasks]
        unique_programmers = list(set(programmers))
        return unique_programmers

    def mark_finished(self, id: int):
        ids = [task.id for task in self.tasks]
        if id not in ids:
            raise ValueError
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
        
    def finished_orders(self):
        finished = [task for task in self.tasks if task.completed_check == "FINISHED"]
        return finished
    
    def unfinished_orders(self):
        unfinished = [task for task in self.tasks if task.completed_check == "NOT FINISHED"]
        return unfinished
    
    def status_of_programmer(self, programmer: str):
        programmers = [task.programmer for task in self.tasks]
        if programmer not in programmers:
            raise ValueError
        
        finished_tasks = 0
        unfinished_tasks = 0
        finished_workload_sum = 0
        unfinished_worload_sum = 0
        for task in self.tasks:
            if task.programmer == programmer:
                if task.completed_check == "FINISHED":
                    finished_tasks += 1
                    finished_workload_sum += task.workload
                else:
                    unfinished_tasks += 1
                    unfinished_worload_sum += task.workload
        return finished_tasks,unfinished_tasks,finished_workload_sum,unfinished_worload_sum

class OrderBookApplication:

    def __init__(self) -> None:
        self.orderbook = OrderBook()
    
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer = input("programmer: ")
        try:
            workload = int(input("workload(hours): "))
            self.orderbook.add_order(description,programmer,workload)
            print("order added!")
        except ValueError:
            print("erroneous input")
        
            
    def list_finished_tasks(self):
        finished = self.orderbook.finished_orders()
        if len(finished) == 0:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)
    
    def list_unfinished_tasks(self):
        unfinished = self.orderbook.unfinished_orders()
        if len(unfinished) == 0:
            print("all tasks finished")
        else:
            for task in unfinished:
                print(task)

    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.orderbook.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")
    
    def programmers(self):
        programmers = self.orderbook.programmers()
        for programmer in programmers:
            print(programmer)
    
    def status_of_programmer(self):
        try:
            programmer = input("programmer: ")
            finished_tasks,unfinished_tasks,finished_workload_sum,unfinished_worload_sum = self.orderbook.status_of_programmer(programmer)
            print(f"finished tasks: {finished_tasks}\nfinished hours: {finished_workload_sum}\nunfinished tasks: {unfinished_tasks}\nhours remaining: {unfinished_worload_sum}")
        except ValueError:
            print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                print("exiting...")
                exit()
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()

application = OrderBookApplication()
application.execute()



