from random import random

def visualizationData():
	"""
	Return: List[List[float]] - an (8, 500) array of floats.
		Each row represents a channel, and column a snapshot in time
	"""
	# Placeholder dummy data
	return [[random() for _ in range(500)] for _ in range(8)]

def modelOutput():
	"""
	Return: int, a 0 or a 1 which represents the model output
	"""
	# Placeholder dummy data
	return int(random() > 0.5)