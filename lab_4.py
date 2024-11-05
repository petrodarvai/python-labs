class Film:

    def __init__(self, name, duration, numb_of_reviews, mark_on_IDBM, type):
        self.__name = name
        self.__duration = duration
        self.__numb_of_reviews = numb_of_reviews
        self.mark_on_IDBM = mark_on_IDBM
        self.type = type
# type це вид фільму, наприклад бойовик, драма
        
    def set_name(self, name):
        self.__name = name

    def set_duration(self, duration):
        self.__duration = duration

    def set_numb_of_reviews(self, numb_of_reviews):
        self.__numb_of_reviews = numb_of_reviews
        
    def get_name(self):
        return self.__name
        
    def get_duration(self):
        return self.__duration
        
    def get_numb_of_reviews(self):
        return self.__numb_of_reviews
            
        
    def __repr__ (self):
        return f"Film(Name: {self.__name}, Duration: {self.__duration}, Numbers of reviews: {self.__numb_of_reviews}, Mark on IDBM: {self.mark_on_IDBM}, Type:{self.type})"
        
    def __str__ (self):
        return f"Name: {self.__name}, Duration: {self.__duration}, Numbers of reviews: {self.__numb_of_reviews}, Mark on IDBM: {self.mark_on_IDBM}, Type:{self.type}"
        
    def __del__(self):
        print(f"Film: {self.__name} delated")
        
def main():
    film_1 = Film( "The Shawshank Redemption", 142, 900000, 9.3, "epic" )
    film_2 = Film( "The Godfather", 175, 850000, 9.2, "gangster" )
    film_3 = Film( "The Dark Knight", 152, 800000, 9.0, "superhero")

    print(film_1)
    print(film_2)
    print(film_3)
    
    print(f"type first film: {film_1.type}")
    print(f"name third film: {film_3.get_name()}")

if __name__ == "__main__":
    main()
    # статичний метод, клас метод, атрибути, які належать об'єкту