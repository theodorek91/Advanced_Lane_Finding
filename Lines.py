class Line:
	
	def __init__(self, image):
		self.img = image
		
	def get_undistort(self, mtx,dist):
		return cv2.undistort(self.img, mtx, dist, None, mtx)