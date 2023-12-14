convert  circles.png -gravity North  -pointsize 26 -fill dodgerblue  -stroke navy    -annotate +0+10 "Classement des hits\n les plus diffusés\n\nsur metis fm" somecaption.gif
magick -background lightblue -fill blue \
	            -font Ravie -pointsize 24 -size 360x \
		              caption:"Here I use caption to wordwrap.\nTwo separate lines." \
			                caption_multi_line.gif
 magick -background lightblue -fill blue -font Candice -size 320x140 \
	           caption:'This text is resized to best fill the space given.' \
		             caption_filled.gif



convert -page +0+0 iphone.png -page +100+0 somecaption.gif -page +500+100 metisfmlogo.png -background lightblue -layers merge +repage classementhi.jpg
