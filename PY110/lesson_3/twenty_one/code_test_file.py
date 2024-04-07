def get_reach_hit_percentage(simulation_results):
    hits_past = [simulation_results[num][3]
        for num in range(len(simulation_results))]
    hits_at_level = []
    running_total = 0

    for num in hits_past:
        running_total += num
        hits_at_level.append(running_total)

    # % chance of reaching a level without busting
    level_total = [sum(data[:-1]) for data in simulation_results.values()]
    aggregate_level = [(level_total[idx] + hits_at_level[idx - 1]) if idx != 0
                       else level_total[idx]
                       for idx in range(len(level_total))]
        
    chance_to_level = [(level_total[idx]/aggregate_level[idx])
                        for idx in range(len(aggregate_level))]

        
    return chance_to_level

def get_win_percentage(simulation_results):
    local_win_ratios = [(data[0] / sum(data[:-1])) if key != 0
                else data[0]/ sum(data[:-1])
                for key, data in simulation_results.items()]
    
    print(local_win_ratios)
    
    percentage_to_hit_level = get_reach_hit_percentage(simulation_results)

    print(percentage_to_hit_level)

    global_win_ratios = [(local_win_ratios[idx] *
                          percentage_to_hit_level[idx])
                          for idx in range(len(local_win_ratios))]
    
    return global_win_ratios


print(get_win_percentage({0:[125, 0, 454, 579], 
                            1: [186, 48, 113, 348],
                            2: [50, 9, 10, 70],
                            3: [2, 0, 0, 3]
                            }))
