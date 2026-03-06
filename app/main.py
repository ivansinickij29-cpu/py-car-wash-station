class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: int, count_of_rating: int) ->None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_rating = count_of_rating
        self.total_income = 0


    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power <= car.clean_mark:
            return 0
        price = car.comfort_class * (
                self.clean_power - car.clean_mark
        ) * self.average_rating / self.distance_from_city_center
        return price

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark > self.clean_power:
            car.clean_mark = self.clean_power

    def serve_car(self, car: Car) -> float:
        if car.clean_mark > self.clean_power:
            price = car.comfort_class * (
                        self.clean_power - car.clean_mark
            ) * self.average_rating / self.distance_from_city_center
            self.total_income += price
            self.wash_single_car(car)
            return price
        return 0

    def rate_service(self, rate: float) -> float:
        new_price = (self.average_rating * self.count_of_rating + rate) / (self.count_of_rating + 1)
        self.count_of_rating += 1
        self.average_rating = new_price
        return new_price



