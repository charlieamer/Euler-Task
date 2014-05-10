
def pictureShower(url, cookies = None):
	import urllib2
	try:
		import PIL.Image as Image
		from StringIO import StringIO
		print('Downloading image ...')
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
		urllib2.install_opener(opener)
		im = Image.open(StringIO(urllib2.urlopen(url).read()))
		im = im.resize((150,30),Image.ANTIALIAS)
		#im.show()
		red = ""
		for y in range(im.size[1]):
			for x in range(im.size[0]):
				red += " " if im.getpixel((x,y))[0] > 150 else "#"
			print (red)
			red = ""
	except:
		#TODO WHAT TO DO IF PIL IS NOT INSTALLED
		raise

