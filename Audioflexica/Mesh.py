import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys
from opensimplex import OpenSimplex

class Mesh:
	def __init__(self):
		self.app = QtGui.QApplication(sys.argv)
		self.view = gl.GLViewWidget()

		verts = []
		faces = []

		#32 by 32 vertices
		for x in range(32):
			for y in range(32):
				verts.append([x, y, 0])
		verts = np.array(verts)


		#implementing faces
		for i in range(31):
			for j in range(31):
				faces.append([i * 32 + j, i *32 + j + 1, i * 32 + j + 32])
				faces.append([ i *32 + j + 1, i * 32 + j + 32 + 1, i * 32 + j + 32])
		faces = np.array(faces)

		colors = np.random.rand(len(faces), 4)
		colors = np.array(colors)

		self.mesh = gl.GLMeshItem(vertexes= verts, faces= faces, faceColors= colors)

		self.view.show()
		self.view.setWindowTitle("Mesh")
		self.mesh.setGLOptions("additive")
		self.view.addItem(self.mesh)


	def run():
		if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
			QtGui.QApplication.instance().exec_()

if __name__ == '__main__':
	mesh = Mesh()
	Mesh.run()



