import sys
import codelib as cl


class Tree:
    def __init__(self, tl, tr):
        self.tl = tl
        self.tr = tr
        self.par = None
        tl.par = self
        tr.par = self
        self.refresh()

    def refresh(self):
        self.h = max(self.tl.get_h(), self.tr.get_h()) + 1
        self.m = max(self.tl.get_m(), self.tr.get_m())
        if self.par is not None:
            self.par.refresh()

    def get_h(self):
        return self.h

    def get_m(self):
        return self.m

    def get_mag(self):
        return 3*self.tl.get_mag() + 2*self.tr.get_mag()

    def swap_l(self, tl):
        self.tl = tl
        tl.par = self
        self.refresh()

    def swap_r(self, tr):
        self.tr = tr
        tr.par = self
        self.refresh()

    def explode(self):
        self.explode_l(self.tl.val)
        self.explode_r(self.tr.val)

    def explode_l(self, val):
        p = self
        while True:
            if p.par is None:
                return
            elif p is p.par.tr:
                p = p.par.tl
                break
            else:
                p = p.par
        while not isinstance(p, Leaf):
            p = p.tr
        p.val += val
        p.par.refresh()

    def explode_r(self, val):
        p = self
        while True:
            if p.par is None:
                return
            elif p is p.par.tl:
                p = p.par.tr
                break
            else:
                p = p.par
        while not isinstance(p, Leaf):
            p = p.tl
        p.val += val
        p.par.refresh()

    def red(self):
        if self.get_h() > 4:
            self.red_h(4)
            return True
        elif self.get_m() > 9:
            self.red_m()
            return True
        return False

    def red_h(self, thres):
        if self.tl.get_h() >= thres:
            if thres == 1:
                self.tl.explode()
                self.swap_l(Leaf(0))
            else:
                self.tl.red_h(thres-1)
        else:
            if thres == 1:
                self.tr.explode()
                self.swap_r(Leaf(0))
            else:
                self.tr.red_h(thres-1)

    def red_m(self):
        if self.tl.get_m() > 9:
            if isinstance(self.tl, Leaf):
                self.swap_l(self.tl.split())
            else:
                self.tl.red_m()
        else:
            if isinstance(self.tr, Leaf):
                self.swap_r(self.tr.split())
            else:
                self.tr.red_m()


class Leaf(Tree):
    def __init__(self, val):
        self.val = val

    def get_h(self):
        return 0

    def get_m(self):
        return self.val

    def get_mag(self):
        return self.val

    def split(self):
        val_l = self.val // 2
        val_r = (self.val+1) // 2
        return Tree(Leaf(val_l), Leaf(val_r))


def parse(x, i):
    if x[i] == '[':
        tl, i = parse(x, i+1)
        tr, i = parse(x, i+1)
        return Tree(tl, tr), i+1
    else:
        return Leaf(int(x[i])), i+1


t = None
for line in sys.stdin:
    x = line.strip()
    if t is None:
        t, i = parse(x, 0)
    else:
        t2, i = parse(x, 0)
        t = Tree(t, t2)
        while t.red():
            pass

print(t.get_mag())
