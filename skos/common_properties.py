import skos


class CommonPropertiesMixin:
    def __init__(self, uri):
        self.uri = uri
        self.label = skos.get_label(uri)
        self.description = skos.get_description(uri)
        self.class_types = skos.get_class_types(uri)
        self.change_note = skos.get_change_note(uri)
        self.alt_labels = skos.get_alt_labels(uri)
        self.created = skos.get_created_date(uri)
        self.modified = skos.get_modified_date(uri)
        self.properties = skos.get_properties(uri)
