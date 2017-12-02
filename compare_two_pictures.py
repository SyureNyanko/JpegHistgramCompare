#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""hist matching."""

import cv2
import numpy as np
import sys
import os.path

def histgram(imgpath):
	
	img = cv2.imread(imgpath)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	hdims = [256]
	ranges = [0, 256]
	ret = cv2.calcHist([img], [0], None, hdims, ranges)
	print(imgpath)
	return ret


if __name__=='__main__':
	argvs = sys.argv  # コマンドライン引数を格納したリストの取得
	argc = len(argvs) # 引数の個数
	print(argc)
	if(argc != 3):
		print("Usage : similar_rate.py Imagepath.jpg Imagepath2.jpg")
		quit()
	ext = os.path.splitext(argvs[1])[1]
	if not (ext == '.jpg' or ext == '.jpeg' or ext == '.JPG' or ext == '.JPEG'):
		print("JPG is missing" )
		print("Usage : similar_rate.py Imagepath.jpg Imagepath2.jpg")
		quit()

	# CV_COMP_CORREL
	# CV_COMP_CHISQR
	# CV_COMP_INTERSECT
	# CV_COMP_BHATTACHARYYA
	
	result = cv2.compareHist(histgram(argvs[1]), histgram(argvs[2]), cv2.HISTCMP_CORREL)
	print(result)
	
	