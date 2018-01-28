from queueBasis.queue import Queue
import random

class Printer:

    # ppm - page per minute
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_mission = None
        self.time_remaining = 0

    def timer(self):
        if self.current_mission != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_mission = None

    def busy(self):
        if self.current_mission != None:
            return True
        else:
            return False

    def next_mossion(self, new_mission):
        self.current_mission = new_mission
        self.time_remaining = new_mission.get_pages() * 60 / self.pagerate


class Mission():
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_time(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp


def simulation(seconds, ppm):

    printer = Printer(ppm)
    print_queue = Queue()
    wait_time = []

    for current_time in range(seconds):
        if new_print_mission():
            mission = Mission(current_time)
            print_queue.enqueue(mission)

        if (not printer.busy()) and (not print_queue.isEmpty()):
            next_mission = print_queue.dequeue()
            wait_time.append(next_mission.wait_time(current_time))
            printer.next_mossion(next_mission)

        printer.timer()

    ave_time = sum(wait_time) / len(wait_time)
    print("Average Wait %6.2f secs %3d tasks remaining." % (ave_time, print_queue.size()))


def new_print_mission():
    num = random.randrange(1, 181)

    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)