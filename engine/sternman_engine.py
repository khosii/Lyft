from engine import Engine

class SternmanEngine(Engine):
    def needs_service(self, warning_light_is_on):
        return warning_light_is_on
