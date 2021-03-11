import numpy
from matplotlib import pyplot as plt

class minkowski:
  def mink_diagram:
    fig = plt.figure(figsize=[14,14])
    x = np.arange(-10,11)
    y = np.sqrt(x**2)
    plt.plot(x,y,'y-')
    plt.plot(x,-y,'y-')
    ax = fig.add_subplot(1, 1, 1)
    plt.annotate('d', (9,-1), fontsize = 13)
    plt.annotate('ct', (-1,9),fontsize = 13)

    gamma = math.sqrt(1/(1-v**2))
    dprime = gamma*(d1 - v*t)
    tprime = gamma*(t - v*d)
    alpha = math.atan(v)
    d = np.abs(d)
    plt.fill_between(x,y,color = 'blue')
    plt.fill_between(x,-y,color = 'blue')
    plt.fill_between(np.arange(-10,11,1),np.repeat(10,21),y,color = 'grey')
    plt.fill_between(np.arange(-10,11,1),np.repeat(-10,21),-y,color = 'grey')
    plt.text(-7.5,1,'space-like', fontsize = 13)
    plt.text(1,-7.5,'time-like', fontsize = 13)

    plt.arrow(0, 0,9,0,width= 0.05,color = 'k')
    plt.arrow(0,0,0,9,width= 0.05,color = 'k')
    plt.arrow(0, 0,-9,0,width= 0.05,color = 'k')
    plt.arrow(0,0,0,-9,width= 0.05,color = 'k')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    plt.annotate('ct(prime)', (9*math.sin(alpha)+0.2,9*math.cos(alpha)), fontsize = 13)
    plt.annotate('d(prime)', (9*math.cos(alpha)-0.5,9*math.sin(alpha)+0.2) ,fontsize = 13)


    plt.arrow(0,0,9,9*math.atan(v),width = 0.05)
    plt.arrow(0,0,9*math.atan(v),9,width = 0.05)
    plt.arrow(0,0,-9*math.atan(v),-9,width = 0.05,)
    plt.arrow(0,0,-9,-9*math.atan(v),width = 0.05)

    plt.plot(0,0,'ro',markersize = 12)
    plt.annotate('A',(0.2,-0.5),color = 'black',size = 12)

    plt.plot(d,t,'ro',markersize = 12)
    plt.annotate('B',(d+0.2,t-0.5),color = 'black',size = 12)

    plt.plot(np.arange(0,d,0.1),np.repeat(t,10*d),'k--')
    plt.plot(np.repeat(d,10*t),np.arange(0,t,0.1),'k--')

    plt.plot((tprime*math.sin(alpha),d),(tprime*math.cos(alpha),t),'g--')
    plt.plot((dprime*math.cos(alpha),d),(dprime*math.sin(alpha),t),'g--')

    plt.annotate('tprime',(tprime*math.sin(alpha)+0.1,tprime*math.cos(alpha)-.2))
    plt.annotate('dprime', (dprime*math.cos(alpha)+0.1,dprime*math.sin(alpha)-0.2))

    rdp = np.round(dprime,5)
    rdt = np.round(tprime,5)
    rgam = np.round(gamma,5)
    plt.annotate('d_prime =' +str(rdp),(1,10.70) )
    plt.annotate('t_prime =' +str(rdt),(1,10.25) )
    plt.annotate('gamma =' +str(rgam),(-4,10.25) )
    plt.annotate('velocity =' +str(v) +'c',((-4,10.70) ))
    plt.title("Minkowski Diagram", fontstyle = 'italic', fontfamily = 'cursive',fontsize = 18)
    plt.show()

