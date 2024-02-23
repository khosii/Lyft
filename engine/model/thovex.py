from datetime import datetime

from car import Car

class Thovex(Car):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


#okay so basically all these classes are checking if the engine should be serviced 
#or not according to the requirements