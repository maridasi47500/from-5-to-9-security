convert -background lightblue -fill blue -size 320x140 \
	                   caption:"$1" \
			                                ./uploads/caption_filled.gif

convert -page +50+10 ./uploads/caption_filled.gif -page +100+150 "./uploads/$2" -page +500+100 ./cado/metisfmlogo.png -background lightblue -layers merge +repage "./uploads/$3"
