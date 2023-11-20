import pstats
# Replace 'test_profile.prof' with the actual path to your .prof file
profiling_results_file = 'test_profile.prof'

# Create a Stats object
stats = pstats.Stats(profiling_results_file)

# Display the statistics
stats.strip_dirs().sort_stats('cumulative').print_stats()

# You can also save the results to a text file for further analysis
stats.strip_dirs().sort_stats('cumulative').dump_stats('profile_results.txt')