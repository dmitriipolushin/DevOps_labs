
class Visits():

    def get_visits(self):
        with open('logs/visits.log', 'r') as fp:
            return fp.read()

    def add_visits(self, time):
        with open('logs/visits.log', 'a') as fp:
            fp.write(time)
            fp.write('\n')
