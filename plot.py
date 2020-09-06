
import matplotlib.pyplot as plt

#plt.style.use('bmh')

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams['lines.linewidth'] = 1

#SIZE = 7
plt.rcParams['axes.labelsize'] = 1
# plt.rcParams['ytick.labelsize'] = SIZE
# plt.rcParams['xtick.labelsize'] = SIZE
#plt.rcParams["font.size"] = 2

COLOR = '1'
plt.rcParams['text.color'] = '#373c4c'
#plt.rcParams['axes.labelcolor'] = "#96989A"
plt.rcParams['xtick.color'] = COLOR
plt.rcParams['ytick.color'] = COLOR


plt.rcParams['grid.linewidth']=0.1
plt.rcParams['grid.color']="0.3"
# plt.rcParams['lines.color']="0.5"
# plt.rcParams['axes.edgecolor']="0.2"
# plt.rcParams['axes.linewidth']=0.5

plt.rcParams['figure.facecolor']="#131722" #Para la parte de afuera
plt.rcParams['axes.facecolor']="#131722" #Para la parte de dentro
# plt.rcParams["savefig.dpi"]=120
# dpi = plt.rcParams["savefig.dpi"]
# width = 700
# height = 1200
# plt.rcParams['figure.figsize'] = height/dpi, width/dpi
#plt.rcParams["savefig.facecolor"] ="#101622"
# plt.rcParams["savefig.edgecolor"]="#101622"

#plt.rcParams['legend.fontsize'] = SIZE
# plt.rcParams['legend.title_fontsize'] = SIZE + 1
# plt.rcParams['legend.labelspacing'] =0.25
# plt.rcParams['image.cmap']='tab10'