class Seq:
    def __init__(self, id, seq):
        self.id = id
        self.seq = seq

    def __add__(self, op2):
        new_id = "Seq(" + self.id + "_" + op2.id + ")"
        return Seq(new_id, self.seq + op2.seq)

    def __mul__(self, n: int):
        return Seq(self.id, self.seq * n)

    def __eq__(self, op2):
        return self.seq == op2.seq

    def __str__(self):
        return ">" + self.id + "\n" + self.seq

    def __bool__(self):
        return self.seq != ""
