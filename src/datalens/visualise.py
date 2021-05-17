import random
from datalens.app import *

# Prevent system exit, close the window properly
# Put QT window infront of notebook tab 
# Add annotations 
# Add functionalities to support different file extensions 
	# Images - png, jpg, jpeg
	# Annotations - COCO, Kitti etc
				# - .txt, .json, graphxml
# Support for segmentation and classification  

class Visualise():
	def __init__(self, 
		datatype='images', 
		task='detection', 
		image_dir_path=None
		):

		self.datatype = datatype
		self.task = task 
		self.image_dir_path = image_dir_path

	# def show(self):#show_image_dir_path(self, imageList, annotationList):
		assert self.image_dir_path != None
		# Load images and annotations
		paths = glob.glob(os.path.join(self.image_dir_path, "*.jpg"))
		imageList = [cv2.imread(path) for path in paths]

		app = QApplication(sys.argv)
		win = AppWindow(imageList)
		win.show()
		app.exec_() # sys.exit(app.exec_())


	# def show_from_list(self, imagePathList, annotationPathList):
