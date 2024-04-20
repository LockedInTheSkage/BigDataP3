
# Default DGIM parameters

stream_path = 'data/my_stream.txt'

# The window size
N = 500

def print_progress_bar(i, N):
    """
    Prints a progress bar to the console to visually indicate the progress of a task.

    The progress bar is colored and updates dynamically in the terminal, providing a visual and numerical 
    indication of the task's completion percentage. The function is designed to be called within a loop to 
    update the progress bar in place.

    Args:
        i (int): The current progress of the task (e.g., the current loop iteration number). 
                 Should start at 0 and go up to N-1.
        N (int): The total number of iterations the task will perform, representing 100% completion.

    Returns:
        None: This function does not return a value but prints the progress bar to the standard output.
    """
    bar_length = 40
    progress = i / N
    num_bar_filled = int(bar_length * progress)
    bar = '\033[35m#' * num_bar_filled + '\033[0m-' * (bar_length - num_bar_filled)
    percent_complete = progress * 100
    print(f'[{bar}] {percent_complete:.1f}% Complete', end='\r')

def dgim_algorithm(stream_path, N):
    
    # Create the buckets and initialize the timestamp
    pos=1
    bucket_list=[[]]


    # Loop through the entire data stream, one bit at a time
    with open(stream_path) as f:
        while True:
            bit = f.read(1)
            
            # Clause to break while loop at the end of the stream
            if not bit:
                break
            
            if bit=="1":
                bucket_list[0].append(pos)
                for b_index, bucket in enumerate(bucket_list):
                    if len(bucket)==3:
                        if len(bucket_list)>b_index+1:
                            bucket_list[b_index+1].append(bucket[1])
                            bucket_list[b_index]=[bucket[2]]
                        else:
                            bucket_list.append([bucket[1]])
                            bucket_list[b_index]=[bucket[2]]
                    else:
                        break
            if len(bucket_list[0])>4:
                break

            pos+=1

    end_time_stamp=pos
            
                            
    return bucket_list, end_time_stamp

bucket = dgim_algorithm(stream_path, N)

print(f"The updated list of timestamps buckets from DGIM algorithm: \n {bucket[0]}")
print(f"The end timestamp: {bucket[1]}")   