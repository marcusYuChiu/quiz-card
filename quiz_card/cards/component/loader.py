"""
For many use cases, each of service only require specific data
"""
from datetime import timedelta, datetime


from quiz_card.cards.models import Card, MemoryStatus


#what do i need for practice service
def get_specific_data(*args):
    pass


def check_color(memory_color):
    '''
    :argument:memory_color:the color which represent memory status
    '''
    if memory_color not in [color.value for color in MemoryStatus]:
        raise ValueError("Unknow memory color: {}".format(memory_color))
    return True


def load_data(memory_color):
    return Card.query.filter_by(memory_status)


def get_date(time):
    return (datetime.today().day - time)


# todo:
    # load data according to color and time and weight
        # note: 
              # time > weight > less practice
              # weight is persent format

class Loader:
    def __init__(self, *args, **kwargs):
        self.color = kwargs['color']
        self.data = None


    def load(self):
        # get data with color which client offer
        self.data = (Card.query.filter(Card.memory_status == self.color)
                               # data is selected by it's create time which minus 3 and
                               # weight is lower than 70
                               .filter((Card.created_time > get_date(3)) |
                                       (Card.weight < 70.0))
                               .order_by(Card.id.desc()))
#        cards = Card.query.filter(Card.memory_status == self.color)



