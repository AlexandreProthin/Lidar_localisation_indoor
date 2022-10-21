import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from rplidar import RPLidar
import time
import matplotlib.animation as animation
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn import decomposition
from sklearn import datasets


# définition de l'utilisation de l'usb pour la communication avec le lidar
lidar = RPLidar('/dev/ttyUSB0')

def PolarToCart(angle,distance):
    """
    Changement de système de coordonnées, polaire vers cartésien
    """
    x = distance*np.cos(angle*((2*np.pi)/360))
    y = distance*np.sin(angle*((2*np.pi)/360))
    return [x,y]

def animate(i, xs, ys):
    """ 
    Tracé du résultat de la détection
    """
    # Limit x and y lists to 20 items
    #xs = xs[-20:]
    #ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.scatter(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Lidar')
    plt.ylabel('Distance')

def dbscan(res):
    """ 
    L'utiliation de la méthode de cluste DBSCAN paermet de grouper les ammas de points 
    """
    # Numpy array of all the cluster labels assigned to each data point
    res = np.array(res)
    std = StandardScaler()
    X = std.fit_transform(res)
    # le réglage des paramètres interne à déjà été réalisé mais peut être modifié pour un cas spécifique
    db = DBSCAN(eps=0.2, min_samples=20).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    results, = []
    # association des labels aux clusters
    for k in zip(unique_labels):
        class_member_mask = labels == k
        Scluster = std.inverse_transform(X[class_member_mask & core_samples_mask])
        results.append(Scluster)
       
    return results

# initialisation pour l'animation
t= time.time()
plt.ion()

while True:
    
    res=[]
    #prise de 3 mesure
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i+1, len(scan)))
        for j in range(len(scan)):
            if scan[j][0] > 10:
                res.append([scan[j][1],scan[j][2]])
        # execution du clustering
        points = dbscan(res)
        # affichage des clusters les uns après les autres
        fig = plt.figure(1)
        ax = fig.add_subplot(1, 1, 1)      
        for i in range(len(points)-1):   
            m = points[i]
            ax.scatter(m[:,0], m[:,1])
            #fig.canvas.draw()
            #ani = animation.FuncAnimation(fig, animate, fargs=(m[:, 0], m[:, 1]), interval=1000)
        time.sleep(1)

        # arret de la démo après 30 secondes d'exécution
        if time.time()-t>30:
            lidar.stop()
            lidar.stop_motor()
            break





