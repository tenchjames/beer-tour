import os


class Repository():
    def __init__(self, file_path, entity_name, columns, reader, writer):
        self.file_path = file_path
        self.entity_name = entity_name
        self.entities = []
        self.entities_by_id = {}
        self.next_id = 1
        self.columns = columns
        self.reader = reader
        self.writer = writer

    def before_insert(self, entity):
        pass

    def before_update(self, entity):
        pass

    def before_delete(self, entity):
        pass

    def after_load(self):
        pass

    def load(self):
        if self.file_path is None:
            self.after_load()
            return
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, "r") as f:
            for line in f:
                entity = self.reader(line)
                if entity.id is None:
                    raise Exception("Id is required")
                id = entity.id

                if int(id) >= self.next_id:
                    self.next_id = int(id) + 1
                self.entities.append(entity)

            for entity in self.entities:
                self.entities_by_id[entity.id] = entity
        self.after_load()

    def insert(self, entity):
        self.before_insert(entity)
        if entity.id != -1 and self.entities_by_id.get(entity.id) is not None:
            return self.entities_by_id[entity.id].clone()

        for e in self.entities:
            if e == entity:
                return e.clone()
        cloned = entity.clone()
        if cloned.id == -1:
            cloned.id = self.next_id
            self.next_id += 1
        self.entities.append(cloned)
        self.entities_by_id[cloned.id] = cloned
        # todo: save to the file
        with open(self.file_path, "a") as f:
            f.write(self.writer(cloned))
        return cloned.clone()

    def update(self, entity):
        if entity.id == -1 or self.entities_by_id.get(entity.id) is None:
            raise Exception("Person does not exist")
        # if this is alreadyfound just return (could be duplicate update)
        for e in self.entities:
            if e == entity:
                return
        current = self.entities_by_id[entity.id]
        # todo: this doesnt work, need to use fields array
        for field in self.fields:
            if getattr(entity, field) is None:
                raise Exception(f"Field {field} is required")
            current.__setattr__(field, getattr(entity, field))
        return current.clone()

    def delete(self, id):
        if self.entities_by_id.get(id) is None:
            return
        entity = self.entities_by_id[id]
        self.entities.remove(entity)
        del self.entities_by_id[id]
        # has to be a smarter way to do this
        with open(self.file_path, "w") as f:
            for e in self.entities:
                if e.id != id:
                    f.write(self.writer(e))

    def find_by_id(self, id):
        if self.entities_by_id.get(id) is None:
            return None
        return self.entities_by_id[id].clone()

    def find_all(self):
        return list(map(lambda e: e.clone(), self.entities))
