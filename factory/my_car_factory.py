from car_factory import CarFactory
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car


class MyCarFactory(CarFactory):
    def create_car(self, car_type, **kwargs):
        car_creation = {
            "Calliope": self._create_calliope,
            "Glissade": self._create_glissade,
            "Palindrome": self._create_palindrome,
            "Rorschach": self._create_rorschach,
            "Thovex": self._create_thovex
        }
        create_car = car_creation.get(car_type)
        if create_car:
            return create_car(**kwargs)
        else:
            raise ValueError(f"Invalid car type: {car_type}")
        
    def _create_calliope(self, **kwargs):
        engine = CapuletEngine(**kwargs)
        battery = SpindlerBattery(**kwargs)
        return Car(engine, battery)
    
    def _create_glissade(self, **kwargs):
        engine = WilloughbyEngine(**kwargs)
        battery = SpindlerBattery(**kwargs)
        return Car(engine, battery)
    
    def _create_palindrome(self, **kwargs):
        engine = SternmanEngine(**kwargs)
        battery = SpindlerBattery(**kwargs)
        return Car(engine, battery)
    
    def _create_rorschach(self, **kwargs):
        engine = WilloughbyEngine(**kwargs)
        battery = NubbinBattery(**kwargs)
        return Car(engine, battery)

    def _create_thovex(self, **kwargs):
        engine = CapuletEngine(**kwargs)
        battery = NubbinBattery(**kwargs)
        return Car(engine, battery)
    

