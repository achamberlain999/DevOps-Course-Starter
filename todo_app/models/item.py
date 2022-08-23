class Item:
    def __init__(self, id, name, description, complete = False):
        self.id = id
        self.name = name
        self.description = description
        self.complete = complete

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], card['desc'], list['name'] == 'Done')