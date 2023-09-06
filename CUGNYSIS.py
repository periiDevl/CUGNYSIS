import psutil
import subprocess
import matplotlib.pyplot as plt
import time

def get_process_data(process_name):
    cpu_usage = []
    ram_usage = []
    gpu_usage = []
    
    for _ in range(num_data_points):
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process_info = psutil.Process(process.info['pid'])
                cpu_usage.append(process_info.cpu_percent(interval=1))
                ram_percent = psutil.virtual_memory().percent
                ram_usage.append(ram_percent)
                
                result = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits',
                                         f'--id={gpu_id}'], stdout=subprocess.PIPE, universal_newlines=True)
                gpu_usage.append(int(result.stdout.strip()))
        
        if not cpu_usage:
            cpu_usage.append(0)
            ram_usage.append(0)
            gpu_usage.append(0)
        
        plt.clf() 
        plt.plot(cpu_usage, label='CPU Usage', linestyle='-', marker='o')
        plt.plot(ram_usage, label='RAM Usage', linestyle='-', marker='o')
        plt.plot(gpu_usage, label='GPU Usage', linestyle='-', marker='o')
        plt.xlabel('Time')
        plt.ylabel('Usage (%)')
        plt.legend(loc='upper right')
        plt.title(f'{process_name} CPU, RAM, and GPU Usage')
        plt.grid(True)
        
        plt.pause(0.1) 

num_data_points = 50

process_name = 'Vision_engine.exe'

gpu_id = 0

fig = plt.figure(figsize=(10, 5))
fig_manager = plt.get_current_fig_manager()

fig_manager.window.setWindowTitle("CUGNYSIS")

get_process_data(process_name)

plt.show()
