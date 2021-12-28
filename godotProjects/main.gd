extends Node

onready var sprite = preload("res://fiddlesworth.tscn")

func _ready():
	for i in range(200):
		var s = sprite.instance() 
		add_child(s)

	pass

