from demo.library import Base

# assert(hasattr(Base, 'read'))  # 先判斷該物件是否有該屬性 使用父類


class FileStream(Base):
    # def get(self):
    #     self.read()
    def read(self):
        print('sub read')

    def write(self):
        print('sub read')


if __name__ == '__main__':
    f = FileStream()
    f.read()
