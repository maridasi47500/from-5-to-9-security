convert  circles.png -gravity North  -pointsize 26 -fill dodgerblue  -stroke navy    -annotate +0+10 "Classement des hits\n les plus diffusés\n\nsur metis fm" somecaption.gif



convert -page +0+0 iphone.png -page +100+0 somecaption.gif -page +500+100 metisfmlogo.png -background lightblue -layers merge +repage classementhi.jpg
