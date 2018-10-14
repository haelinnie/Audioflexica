import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys

class Mesh:
	def __init__(self):
		self.app = QtGui.QApplication(sys.argv)
		self.view = gl.GLViewWidget()

		verts = np.array([
		[ 0,  0,  0],
		[ 1,  0,  0],
		[ 1,  1,  0],
		[ 0,  1,  0],
		[ 0,  0,  1],
		[ 1,  0,  1],
		[ 1,  1,  1],
		[ 0,  1,  1],])

		faces = np.array([
		[0, 1, 2],
		[0, 2, 3],
		[0, 1, 4],
		[1, 5, 4],
		[1, 2, 5],
		[2, 5, 6],
		[2, 3, 6],
		[3, 6, 7],
		[0, 3, 7],
		[0, 4, 7],
		[4, 5, 7],
		[5, 6, 7],])

		colors = np.array([
		[1,  0, 0, .5],
		[0, 1, 0, .5],
		[0, 0, 1, .5],
		[1, 0 , 1, .5],
		[1, 1, 1, .5],
		[0, 1, 1, .5],
		[1, 1, 0, .5],
		[.5, .8, .1 , .5],
		[.7, .1, .9, .5],
		[.7, .2, .6, .5],
		[.8, .1, .5, .5],])

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



