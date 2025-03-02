import matplotlib.pyplot as plt
import autograd.numpy as np

def plotting_data(type: str, data: np.ndarray, num_samples: int, title_str: str, coord_str: list) -> None:
    x = np.linspace(0, num_samples, num_samples)
    _, axes = plt.subplots(1, 3, figsize=(16, 4))
    for i in range(3):
        plot_data = data[i]
        axes[i].plot(x, data[i][:num_samples])
        if(coord_str == None):
            continue
        axes[i].set_title(title_str+ type + " in " + coord_str[i])
    plt.subplots_adjust(wspace=0.3)
    plt.show()

def robot_trajectory_plot(data: np.ndarray, title_str: str, coord_str: list[str]) -> None:
    plt.plot(data[0, :], data[1, :])
    plt.title(title_str)
    plt.xlabel(coord_str[0])
    plt.ylabel(coord_str[1])
    plt.grid()
    plt.show()

def robot_trajectory_plot2(data: np.ndarray, data1:np.ndarray,  title_str: str, coord_str: list[str], label) -> None:
    plt.plot(data[0, :], data[1, :], label=label[0])
    plt.plot(data1[0, :], data1[1, :], label=label[1], linestyle='--')

    plt.title(title_str)
    plt.xlabel(coord_str[0])
    plt.ylabel(coord_str[1])
    
    plt.grid()
    plt.legend()
    plt.show()

def occupancy_plot(data, title_str: str, coord_str: list[str]) -> None:
    plt.imshow(1/(1+np.exp(-data)), cmap='gray', origin='lower')
    plt.title(title_str)
    plt.xlabel(coord_str[0])
    plt.ylabel(coord_str[1])
    plt.show()