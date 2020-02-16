class hashtable():
    def __init__(self):
        self.table = {}

    def __getitem__(self, key):
        try:
            value = self.table[key].pop(-1)
            if self.table[key] == []:
                del self.table[key]
            return value
        except:
            print("Invalid key!")
            return None

    def __setitem__(self, key, value):
        try:
            if self.table[key]:
                self.table[key].append(value)
                print(self.table[key])
        except:
            self.table[key] = []
            self.table[key].append(value)
            print(self.table[key])
    











def main():
    H = hashtable()
    print(H.table == {})
    H[2] = 3
    H[2] = 2
    H[3] = 4

    print("min: ",min(H.table))
    print(H[min(H.table)])
    print(H[min(H.table)])
    print(H[min(H.table)])


    H[2] = 3
    print(H[min(H.table)])

if __name__ == "__main__":
    main()

