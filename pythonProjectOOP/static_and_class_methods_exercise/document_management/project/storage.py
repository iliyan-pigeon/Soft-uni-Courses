class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = [d for d in self.documents if d.id == document_id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)
                break

    def delete_topic(self, topic_id):
        self.topics.remove([t for t in self.topics if t.id == topic_id][0])

    def delete_document(self, document_id):
        self.documents.remove(next(filter(lambda x: x.id == document_id, self.documents)))

    def get_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]
        return document

    def __repr__(self):
        return "\n".join([str(document) for document in self.documents])