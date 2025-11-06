class pet:
    def __init__(self):
        self.name = "kucing"
        self.type = "munchkin"
        self.year = 1

    def info(self):
        print(f"Cat name is :  {self.name}")
        print(f"Cat type is : {self.type}")
        print(f"Cat age is : {self.year}")



kucing = pet()

kucing.name = "noelle"

print(kucing.name)
print(kucing.type)
print(kucing.year)

print(kucing.info())

anjing = pet()

anjing.name = "jule"
anjing.type = "hama"
anjing.year = "dead"

print(anjing.name)
print(anjing.type)
print(anjing.year)

