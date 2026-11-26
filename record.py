class Record:
    def __init__(self, record_id, title):
        self.id = record_id
        self.title = title

    def __str__(self):
        return f"ID={self.id}, Title={self.title}"