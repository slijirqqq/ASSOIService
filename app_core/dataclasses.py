class DataclassMixin:

    @property
    def dto(self):
        return self.__dict__
