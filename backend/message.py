class Message:
    def __init__(self, author, contents):
        self.author = author
        self.contents = contents

    def json(self):
        return {"author-id": self.author, "contents": self.contents}
