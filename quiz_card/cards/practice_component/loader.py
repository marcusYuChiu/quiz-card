"""
For many use cases, each of service only require specific data
"""

from quiz_card.models import Card, MemoryStatus


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


# todo:
    # load data according to color and time and weight
        # note: 
              # time > weight > less practice
              # weight is persentage format

class Loader:
    def __init__(self, *args, **kwargs):
        self.color = kwargs['color']

 
    def load_data(self):
        data = card.query.filter_by(memory_status=self.color)


    def count_to_ten(self):
        pass




