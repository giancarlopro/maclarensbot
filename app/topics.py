import random

class Topic:
    @staticmethod
    def random():
        topics = [
            'memes',
            'john cena',
            '9gag',
            'cute cats',
            'video games',
            'instagram pictures',
            'lifestyle',
            'motivacional',
            'shia labeouf motivacional',
            'e hora do show porra',
            'bambam',
            'how i met your mother',
            'breaking bad',
            'badass',
            'game of thrones',
            'arya stark',
            'starks',
            'web development',
            'cars',
            'motorcycles',
            'comedy',
            'ambient',
            'lakes',
            'mountains',
            'beaches',
            'music clubs',
            'beatbox',
            'drinking',
            'wine',
            'beautiful sunset',
            'moonlite',
            'one piece'
        ]

        return random.choice(topics)
