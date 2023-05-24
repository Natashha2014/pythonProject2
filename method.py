class ParentClass:
    def school(self, a, b):
         return a, b


class ParentClass2:
    def academy(self, x, y):
        return x + y


class ParentClass3(ParentClass2):

    def university(self, y, z):
        return y * z