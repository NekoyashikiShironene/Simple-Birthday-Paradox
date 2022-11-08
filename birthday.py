'''The probability of a shared birthday exceeds 50% in a group of only 23 people.'''

from random import randint

class Birthday:
    def __init__(self, people=23, rounds=1500):
        self.people = people
        self.rounds = rounds

    def get_birthday(self):
        '''Get a random birthday (366 days)'''

        month = randint(1, 12)
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = randint(1, 31)
        elif month == 2:
            day = randint(1, 29)
        else:
            day = randint(1, 30)

        return day, month


    def is_share_birthday(self):
        '''Check each round if at least 2 people have the same birthday.'''

        birthday_list = set(self.get_birthday() for i in range(self.people))
        share_birthday_count = len(birthday_list) != self.people

        return share_birthday_count

    def get_probability(self):
        '''The computed probability of at least two people sharing a birthday versus the number of people'''

        share_birthday_list = list(self.is_share_birthday() for i in range(self.rounds))
        probability = share_birthday_list.count(True) / self.rounds
        return probability


if __name__ == '__main__':
    birthday  = Birthday()
    probability = birthday.get_probability()
    print('Number of people =', birthday.people)
    print('Probability =', probability)
