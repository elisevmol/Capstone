def plot_average(the_data, numbers, clusternumber, dataset):
    
    time_series = zip(*[the_data[n] for n in numbers])

    mean_std = []
    for years in time_series:
        y = [year[1] for year in years]
        mean_std.append([years[0][0], np.mean(y), np.std(y)])
     
    fig = plt.figure(2)
    ax = fig.add_subplot(111, axisbg='black')
    ax.set_axis_bgcolor('black')

    std = [x[2] for x in mean_std]
    y = [x[1] for x in mean_std]
    x = [int(x[0]) for x in mean_std]
    
    plt.errorbar(x, y, std, color='azure', linestyle='-', marker='o', markersize=4, 
                 markerfacecolor='azure', elinewidth=0.5, ecolor='azure')
    
    
    plt.yticks(fontsize = 10, weight='light')
    plt.xticks(fontsize = 10, weight='light')

    plt.gca().set_ylim(bottom=0)
    
    plt.title('Average for Cluster ' + str(clusternumber), fontsize=13)
    #at = '/Users/elise/Documents/Capstone/Graphs/average-' + dataset + str(clusternumber) + '.png'
    #plt.savefig(at)
    plt.show()