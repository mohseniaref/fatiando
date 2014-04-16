"""
3D linear inversion using blocky models (prisms and tesseroids).

**Planting inversion**

>>> import numpy as np
>>> from fatiando import gridder, utils
>>> from fatiando.gravmag import prism
>>> from fatiando.mesher import Prism, PrismMesh
>>> # Create a model
>>> model = [Prism(4000, 6000, 4000, 6000, 1000, 4000, {'density':500})]
>>> # and generate noisy synthetic data
>>> shape = (25, 25)
>>> bounds = [0, 10000, 0, 10000, 0, 5000]
>>> area = bounds[0:4]
>>> x, y, z = gridder.regular(area, shape, z=-1)
>>> gz = utils.contaminate(prism.gz(x, y, z, model), 0.1, seed=0)
>>> # Setup the inversion by creating a mesh and seeds
>>> mesh = PrismMesh(bounds, (5, 10, 10))
>>> seeds = sow([[5000, 5000, 2000, {'density':500}]], mesh)
>>> # Run the inversion
>>> solver = Gravity(x, y, z, gz, mesh).config(
...     'planting', seeds=seeds, compactness=1, threshold=0.001).fit()
>>> # Lets print the solution
>>> for top, layer in zip(mesh.get_zs(), solver.estimate_.reshape(mesh.shape)):
...     print("top: {} m".format(top))
...     print(layer)
top: 0.0 m
[[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]]
top: 1000.0 m
[[   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.  500.  500.    0.    0.    0.    0.]
 [   0.    0.    0.    0.  500.  500.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]]
top: 2000.0 m
[[   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.  500.  500.    0.    0.    0.    0.]
 [   0.    0.    0.    0.  500.  500.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]]
top: 3000.0 m
[[   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.  500.  500.    0.    0.    0.    0.]
 [   0.    0.    0.    0.  500.  500.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]
 [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.]]
top: 4000.0 m
[[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]]


"""
from __future__ import division
import bisect
from math import sqrt

import numpy

from . import prism as prism_engine
from . import tesseroid as tesseroid_engine
from ..utils import safe_dot
from ..inversion.base import Misfit
from ..mesher import Prism, Tesseroid

class Gravity(Misfit):
    def __init__(self, x, y, z, data, mesh, field='gz'):
        super(Gravity, self).__init__(data=data,
            positional=dict(x=x, y=y, z=z),
            model={'mesh': mesh},
            nparams=mesh.size,
            islinear=True)
        self.kernel = None
        if mesh.celltype is Prism:
            self.kernel = getattr(prism_engine, field)
        elif mesh.celltype is Tesseroid:
            self.kernel = getattr(tesseroid_engine, field)
        else:
            raise AttributeError(
                "Invalid mesh celltype '%s'" % (mesh.celltype))
        self.dnorm = numpy.linalg.norm(data)
        self.prop = 'density'
        self._effects = {}

    def _get_predicted(self, p):
        if self._cache['jacobian']['array'] is None:
            x = self.positional['x']
            y = self.positional['y']
            z = self.positional['z']
            mesh = self.model['mesh']
            return numpy.sum(self.kernel(x, y, z, [c], dens=p[i])
                             for i, c in enumerate(mesh) if p[i] != 0)
        else:
            return safe_dot(self.jacobian(None), p)

    def _get_jacobian(self, p):
        x = self.positional['x']
        y = self.positional['y']
        z = self.positional['z']
        mesh = self.model['mesh']
        jac = numpy.empty((self.ndata, self.nparams), dtype=float)
        for i, c in enumerate(mesh):
            jac[:, i] = self.kernel(x, y, z, [c], dens=1)
        return jac

    def shape_of_anomaly(self, p, increment=None):
        if self._parents is None:
            value = self._get_shape_of_anomaly(p, increment)
        else:
            if self._scale is None:
                obj1, obj2 = self._parents
                value = (obj1.shape_of_anomaly(p, increment)
                         + obj2.shape_of_anomaly(p, increment))
            else:
                assert len(self._parents) == 1, \
                    'Result of multiplying Objective produces > one parent.'
                obj = self._parents[0]
                value = self._scale*obj.shape_of_anomaly(p, increment)
        return value

    def _get_shape_of_anomaly(self, p, increment=None):
        predicted = self.predicted(p)
        if increment is not None:
            prop = increment.props[self.prop]
            # Using += alters the cached array
            predicted = predicted + prop*self._get_effect(increment.i)
        alpha = numpy.sum(self.data*predicted)/self.dnorm**2
        return numpy.linalg.norm(alpha*self.data - predicted)

    def _get_value(self, p, **kwargs):
        predicted = self.predicted(p)
        increment = kwargs.get('increment')
        if increment is not None:
            prop = increment.props[self.prop]
            # Using += alters the cached array
            predicted = predicted + prop*self._get_effect(increment.i)
        if self.weights is None:
            value = numpy.linalg.norm(self.data - predicted)
        else:
            value = sqrt(numpy.sum(self.weights*((self.data - predicted)**2)))
        return value/self.dnorm

    def _get_effect(self, index):
        if index not in self._effects:
            x = self.positional['x']
            y = self.positional['y']
            z = self.positional['z']
            mesh = self.model['mesh']
            self._effects[index] = self.kernel(x, y, z, [mesh[index]], dens=1)
        return self._effects[index]

    def config(self, method, **kwargs):
        if method == 'planting':
            if 'seeds' not in kwargs:
                raise AttributeError(
                    "Missing 'seeds' keyword argument for 'planting'")
            if 'compactness' not in kwargs:
                raise AttributeError(
                    "Missing 'compactness' keyword argument for 'planting'")
            if 'threshold' not in kwargs:
                raise AttributeError(
                    "Missing 'threshold' keyword argument for 'planting'")
            self.fit_method = 'planting'
            self.fit_args = dict(seeds=kwargs['seeds'],
                                 compactness=kwargs['compactness'],
                                 threshold=kwargs['threshold'])
            return self
        else:
            return super(Gravity, self).config(method, **kwargs)

    def planting(self, seeds, threshold, compactness):
        mesh = self.model['mesh']
        seeds = [s for s in seeds if self.prop in s.props]
        nseeds = len(seeds)
        estimate = numpy.zeros(self.nparams)
        for seed in seeds:
            estimate[seed.i] = seed.props[self.prop]
        neighbors = []
        for seed in seeds:
            neighbors.append(self._get_neighbors(seed, neighbors, estimate))
        misfit = self.value(estimate)
        goal = self.shape_of_anomaly(estimate)
        compact = 0
        # Weight the regularizing function by the mean extent of the mesh
        mu = compactness*1/(sum(mesh.shape)/3)
        accretions = 0
        for iteration in xrange(mesh.size - nseeds):
            grew = False
            for s in xrange(nseeds):
                best = self._grow(neighbors[s], misfit, goal, compact, mu,
                                  threshold, estimate)
                if best is not None:
                    goal = best['goal']
                    misfit = best['misfit']
                    compact = best['compact']
                    estimate = self._update_cache(best['neighbor'], estimate)
                    neighbors[s].pop(best['neighbor'].i)
                    newneighbors = self._get_neighbors(best['neighbor'],
                                        neighbors, estimate)
                    neighbors[s].update(newneighbors)
                    grew = True
                    accretions += 1
            if not grew:
                break
        return estimate

    def _get_neighbors(self, cell, neighbors, estimate):
        indexes = [n for n in self._neighbor_indexes(cell.i)
                   if not self._is_neighbor(n, cell.props, neighbors)
                   and estimate[n] == 0]
        neighbors = dict(
            (i, Neighbor(i, cell.props, cell.seed,
                         self._distance(i, cell.seed)))
            for i in indexes)
        return neighbors

    def _distance(self, n, m):
        """
        Calculate the distance (in number of cells) between cells n and m.
        """
        ni, nj, nk = self._index2ijk(n)
        mi, mj, mk = self._index2ijk(m)
        return sqrt((ni - mi)**2 + (nj - mj)**2 + (nk - mk)**2)

    def _index2ijk(self, index):
        """
        Transform the index of a cell to a 3-dimensional (i,j,k) index.
        """
        nz, ny, nx = self.model['mesh'].shape
        k = index//(nx*ny)
        j = (index - k*(nx*ny))//nx
        i = (index - k*(nx*ny) - j*nx)
        return i, j, k

    def _is_neighbor(self, index, props, neighborhood):
        """
        Check if index is already in the neighborhood with props
        """
        for neighbors in neighborhood:
            for n in neighbors:
                if index == neighbors[n].i:
                    for p in props:
                        if p in neighbors[n].props:
                            return True
        return False

    def _neighbor_indexes(self, n):
        """Find the indexes of the neighbors of n"""
        mesh = self.model['mesh']
        nz, ny, nx = mesh.shape
        indexes = []
        # The guy above
        tmp = n - nx*ny
        if tmp > 0:
            indexes.append(tmp)
        # The guy below
        tmp = n + nx*ny
        if tmp < mesh.size:
            indexes.append(tmp)
        # The guy in front
        tmp = n + 1
        if n%nx < nx - 1:
            indexes.append(tmp)
        # The guy in the back
        tmp = n - 1
        if n%nx != 0:
            indexes.append(tmp)
        # The guy to the left
        tmp = n + nx
        if n%(nx*ny) < nx*(ny - 1):
            indexes.append(tmp)
        # The guy to the right
        tmp = n - nx
        if n%(nx*ny) >= nx:
            indexes.append(tmp)
        # Filter out the ones that do not exist or are masked (topography)
        return [i for i in indexes if i is not None and mesh[i] is not None]

    def _grow(self, neighbors, misfit, goal, compact, mu, threshold, estimate):
        best = None
        for n in neighbors:
            neighbor = neighbors[n]
            newmisfit = self.value(estimate, increment=neighbor)
            if (newmisfit >= misfit
                or abs(newmisfit - misfit)/misfit < threshold):
                continue
            newcompact = compact + neighbor.distance
            newgoal = (self.shape_of_anomaly(estimate, increment=neighbor)
                       + mu*newcompact)
            if best is None or newgoal < best['goal']:
                best = dict(neighbor=neighbor, goal=newgoal, misfit=newmisfit,
                            compact=newcompact)
        return best

    def _update_cache(self, neighbor, estimate):
        # Update the predicted data in the cache
        predicted = self.predicted(estimate)
        prop = neighbor.props[self.prop]
        predicted += prop*self._get_effect(neighbor.i)
        estimate[neighbor.i] = prop
        hash = self.hasher(estimate)
        self._cache['predicted']['hash'] = hash
        self._cache['predicted']['array'] = predicted
        # Remove the effect from the store because it's no longer needed
        self._effects.pop(neighbor.i)
        return estimate

class PrismSeed(Prism):
    """
    A seed that is a right rectangular prism.
    """

    def __init__(self, i, location, prism, props):
        Prism.__init__(self, prism.x1, prism.x2, prism.y1, prism.y2, prism.z1,
            prism.z2, props=props)
        self.i = i
        self.seed = i
        self.x, self.y, self.z = location

class TesseroidSeed(Tesseroid):
    """
    A seed that is a tesseroid (spherical prism).
    """

    def __init__(self, i, location, tess, props):
        Tesseroid.__init__(self, tess.w, tess.e, tess.s, tess.n, tess.top,
            tess.bottom, props=props)
        self.i = i
        self.seed = i
        self.x, self.y, self.z = location

class Neighbor(object):
    """
    A neighbor.
    """

    def __init__(self, i, props, seed, distance):
        self.i = i
        self.props = props
        self.seed = seed
        self.distance = distance

def sow(locations, mesh):
    """
    Create the seeds given a list of (x,y,z) coordinates and physical
    properties.

    Removes seeds that would fall on the same location with overlapping
    physical properties.

    Parameters:

    * locations : list
        The locations and physical properties of the seeds. Should be a list
        like::

            [
                [x1, y1, z1, {"density":dens1}],
                [x2, y2, z2, {"density":dens2, "magnetization":mag2}],
                [x3, y3, z3, {"magnetization":mag3, "inclination":inc3,
                              "declination":dec3}],
                ...
            ]

    * mesh : :class:`fatiando.mesher.PrismMesh`
        The mesh that will be used in the inversion.

    Returns:

    * seeds : list of seeds
        The seeds that can be passed to
        :func:`~fatiando.gravmag.harvester.harvest`

    """
    seeds = []
    if mesh.celltype == Tesseroid:
        seedtype = TesseroidSeed
    elif mesh.celltype == Prism:
        seedtype = PrismSeed
    for x, y, z, props in locations:
        index = _find_index((x, y, z), mesh)
        if index is None:
            raise ValueError(
                "Couldn't find seed at location (%g,%g,%g)" % (x, y, z))
        # Check for duplicates
        if index not in (s.i for s in seeds):
            seeds.append(seedtype(index, (x, y, z), mesh[index], props))
    return seeds

def _find_index(point, mesh):
    """
    Find the index of the cell that has point inside it.
    """
    x1, x2, y1, y2, z1, z2 = mesh.bounds
    nz, ny, nx = mesh.shape
    xs = mesh.get_xs()
    ys = mesh.get_ys()
    zs = mesh.get_zs()
    x, y, z = point
    if (x <= x2 and x >= x1 and y <= y2 and y >= y1 and
        ((z <= z2 and z >= z1 and mesh.zdown) or
         (z >= z2 and z <= z1 and not mesh.zdown))):
        if mesh.zdown:
            # -1 because bisect gives the index z would have. I want to know
            # what index z comes after
            k = bisect.bisect_left(zs, z) - 1
        else:
            # If z is not positive downward, zs will not be sorted
            k = len(zs) - bisect.bisect_left(zs[::-1], z)
        j = bisect.bisect_left(ys, y) - 1
        i = bisect.bisect_left(xs, x) - 1
        seed = i + j*nx + k*nx*ny
        # Check if the cell is not masked (topography)
        if mesh[seed] is not None:
            return seed
    return None