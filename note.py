from datetime import datetime


class Note:
    id: int
    title: str
    body: str
    date_created: datetime
    date_modified: datetime

    def __init__(self, id: int, title: str, body: str):
        self.id = id
        self.title = title
        self.body = body
        self.date_created = datetime.now()
        self.date_modified = self.date_created

    def __str__(self):
        return (f"ID: {self.id}\n\t\tTitle: {self.title}\n\t\tBody: {self.body}\n"
                f"\t\tCreated: {self.date_created}\n"
                f"\t\tModified: {self.date_modified}\n")
