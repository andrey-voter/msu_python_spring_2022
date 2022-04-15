"""the main module"""
class CustomList(list):
    """the main class"""
    def __init___(self):
        self.data = []
        self.size = 0

    def __add__(self, other):
        tmp = CustomList()
        size = max(len(self), len(other))
        min_size = min(len(self), len(other))
        for i in range(size):
            if i < min_size:
                tmp.append(self[i] + other[i])
            else:
                if size == len(self):
                    tmp.append(self[i])
                else:
                    tmp.append(other[i])
        return tmp

    def __radd__(self, other):
        tmp = CustomList()
        size = max(len(self), len(other))
        min_size = min(len(self), len(other))
        for i in range(size):
            if i < min_size:
                tmp.append(self[i] + other[i])
            else:
                if size == len(self):
                    tmp.append(self[i])
                else:
                    tmp.append(other[i])
        return tmp

    def __sub__(self, other):
        tmp = CustomList()
        size = max(len(self), len(other))
        min_size = min(len(self), len(other))
        for i in range(size):
            if i < min_size:
                tmp.append(self[i] - other[i])
            else:
                if len(self) > len(other):
                    tmp.append(self[i])
                else:
                    tmp.append(-other[i])
        return tmp

    def __rsub__(self, other):
        tmp = CustomList()
        size = max(len(self), len(other))
        min_size = min(len(self), len(other))
        for i in range(size):
            if i < min_size:
                tmp.append(other[i] - self[i])
            else:
                if len(self) > len(other):
                    tmp.append(-self[i])
                else:
                    tmp.append(other[i])
        return tmp

    def summa(self):
        ans = 0
        for i in range(len(self)):
            ans += self[i]
        return ans

    def __eq__(self, other):
        return self.summa() == other.summa()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        ans = ''
        for i in range(len(self)):
            ans += str(self[i])
            ans += ' '
        return "({0}custom_list_sum == {1})".format(ans, str(self.summa()))
