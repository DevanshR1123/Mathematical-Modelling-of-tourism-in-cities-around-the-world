from math import sqrt, fsum


def avg(nl):
    return fsum(nl)/len(nl)


def std(nl):
    mu = avg(nl)
    n = len(nl)
    return sqrt(fsum([(x-mu)**2 for x in nl])/n)


def normalise(v, mu, std):
    return (v-mu)/std


def map_range(vr, rs, re):
    vs, ve = min(vr)-1, max(vr)+1
    return [rs+(v-vs)*(re-rs)/(ve-vs)for v in vr]


def normalise_range(rn, rs, re):
    return map_range([normalise(x, avg(rn), std(rn)) for x in rn], rs, re)
