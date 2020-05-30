'''
	Room Scheduling
	You are given an array of tuples (start, end) representing time intervals for lectures.
	The intervals may be overlapping. Return the number of rooms that are required.

	example. [(30, 75), (0, 50), (60, 150)] should return 2.
	
	Logic: Take Dictionary of all Start Time and End Time
	Run A loop from minimum Start Time to Maximum End TIme
	For every Start Time Add a Class Room and For Every 
	End Time Remove the Class Room 
	
'''

def totalRooms(timingTuples):
	start_times = dict()
	end_times = dict()
	
	for start,end in timingTuples:
		if start not in start_times:
			start_times[start] = 0
		start_times[start] += 1
		
		
		if end not in end_times:
			end_times[end] = 0
		end_times[end] += 1
	
	global_start_time,global_end_time = min(start_times),max(end_times)
	
	max_class_room = 0
	current_class_room = 0
	
	for i in range(global_start_time,global_end_time):
		if i in start_times:
			current_class_room += start_times[i]
			if current_class_room > max_class_room:
				max_class_room = current_class_room
		
		if i in end_times:
			current_class_room -= end_times[i]
			
	return max_class_room


assert totalRooms([(30, 75), (0, 50), (60, 150)]) == 2

assert totalRooms([(30, 60), (10, 20), (61, 150)]) == 1

assert totalRooms([(60,80),(10,30),(25,75)]) == 2