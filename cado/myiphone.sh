convert -size 320x320 xc:lightblue \
          -draw "fill tomato  circle 250,30 310,30 \
                 fill limegreen  circle 55,75 15,80 \
                 font-size 22  decorate UnderLine \
                 fill dodgerblue  stroke navy  stroke-width 2 \
                 translate 10,110 rotate -15 text 10,10 ' Jouez et '" \
          -draw "font-size 22  decorate UnderLine \
                 fill dodgerblue  stroke navy  stroke-width 2 \
                 translate 10,175 rotate -15 text 10,10 ' gagnez votre  '" \
          -draw "font-size 42  decorate UnderLine \
                 fill dodgerblue  stroke navy  stroke-width 2 \
                 translate 10,210 rotate -15 text 10,10 ' iphone 15  '" \
          draw_mvg.gif


convert -page +0+0 iphone.png -page +100+0 draw_mvg.gif -page +500+100 metisfmlogo.png -background lightblue -layers merge +repage gagneziphone1.jpg
