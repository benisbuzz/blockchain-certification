from dataclasses import dataclass

@dataclass
class RequestCertificate:
    flight_number: str
    fuel_supplier: str
    fuel_order_number: str
    offset_quantity: int

class AirlineAccount:
    def init():
        pass
    def get_certificates() -> list[str]:
        pass
    def make_request() -> RequestCertificate:
        pass

class GovernmentAccount:
    def init():
        pass

class VerifierAccount:
    def init():
        pass

class EmissionsAccount:
    def init():
        pass
