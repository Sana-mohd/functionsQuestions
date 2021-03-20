"""def increment(number):
    def inner_increment():
        return number + 1
    return inner_increment()
print(increment(10))



def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power(4)
print(generate_power(3))"""



def mean():
    sample = []
    def inner_mean(number,num):
        sample.append(number)
        sample.append(num)
        return sum(sample) / len(sample)
    return inner_mean(56,87)
print(mean()) 