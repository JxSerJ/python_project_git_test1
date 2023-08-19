from datetime import datetime


class Note:
    id: int
    title: str
    body: str
    date_created: datetime
    date_modified: datetime

    def __init__(self, id: int, title: str, body: str, date_created: datetime = None,
                 date_modified: datetime = None):
        self.id = id
        self.title = title
        self.body = body
        if not date_created:
            self.date_created = datetime.now()
        else:
            self.date_created = date_created
        if not date_modified:
            self.date_modified = datetime.now()
        else:
            self.date_modified = date_modified

    def __str__(self):
        return (f"ID: {self.id}\n\t\tTitle: {self.title}\n\t\tBody: {self.body}\n"
                f"\t\tCreated: {self.date_created.isoformat()}\n"
                f"\t\tModified: {self.date_modified.isoformat()}\n")

    def short_info(self):
        return (f"ID: {self.id}, Title: {self.title}\n"
                f"Last modified: {self.date_modified.isoformat()}\n")

    def update_data(self, title: str, body: str):
        self.title = title
        self.body = body
        self.date_modified = datetime.now()
