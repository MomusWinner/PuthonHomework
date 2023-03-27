def keyword_search(string: str):
    keywords = ['распис', 'трен', 'плат']
    for i in keywords:

        if string.find(i) != -1:
            if i == 'распис':
                gym_inf.schedule_inf()
            elif i == 'трен':
                gym_inf.coach_inf()
            elif i == 'плат':
                gym_inf.price_inf()

def counting_words(string:str):
    return len(string.split())

