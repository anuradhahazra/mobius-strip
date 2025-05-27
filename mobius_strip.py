# mobius_strip.py

import numpy as np
from scipy.integrate import simpson
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class MobiusStrip:
    def __init__(self, R=1.0, w=0.3, n=200):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._generate_mesh()

    def _generate_mesh(self):
        u, v = self.U, self.V
        X = (self.R + v * np.cos(u / 2)) * np.cos(u)
        Y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        Z = v * np.sin(u / 2)
        return X, Y, Z

    def compute_surface_area(self):
        Xu = np.gradient(self.X, axis=1)
        Yu = np.gradient(self.Y, axis=1)
        Zu = np.gradient(self.Z, axis=1)

        Xv = np.gradient(self.X, axis=0)
        Yv = np.gradient(self.Y, axis=0)
        Zv = np.gradient(self.Z, axis=0)

        Nx = Yu * Zv - Zu * Yv
        Ny = Zu * Xv - Xu * Zv
        Nz = Xu * Yv - Yu * Xv

        dA = np.sqrt(Nx**2 + Ny**2 + Nz**2)

        surface_area = simpson(simpson(dA, self.v), self.u)
        return surface_area

    def compute_edge_length(self):
        edge1 = self._edge_points(self.w / 2)
        edge2 = self._edge_points(-self.w / 2)
        return self._curve_length(edge1) + self._curve_length(edge2)

    def _edge_points(self, v_val):
        u_vals = self.u
        x = (self.R + v_val * np.cos(u_vals / 2)) * np.cos(u_vals)
        y = (self.R + v_val * np.cos(u_vals / 2)) * np.sin(u_vals)
        z = v_val * np.sin(u_vals / 2)
        return np.column_stack((x, y, z))

    def _curve_length(self, points):
        return sum(euclidean(points[i], points[i + 1]) for i in range(len(points) - 1))

    def plot(self, save=False):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='none', alpha=0.95)
        ax.set_title('Möbius Strip')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        if save:
            plt.savefig("plot.png")
        try:
            plt.show()
        except KeyboardInterrupt:
            print("Plot closed manually.")

