class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int,
                 count_income: int
                 ) ->None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.total_income = count_income


    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power <= car.clean_mark:
            return 0
        price = car.comfort_class * (
                self.clean_power - car.clean_mark
        ) * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark > self.clean_power:
            car.clean_mark = self.clean_power

    def serve_car(self, cars: Car) -> float:
        if self.clean_power > cars.clean_mark:
            price = self.calculate_washing_price(cars)
            self.total_income += price
            self.wash_single_car(cars)
            return price
        return 0

    def rate_service(self, rate: float) -> float:
        new_price = (self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = new_price
        return new_price



