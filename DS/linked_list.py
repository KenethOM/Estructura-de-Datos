#! /usr/bin/python3
from node import Node


class LinkedList:
    def __init__(self,value = None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node
    
    def insert_new_head(self,new_value):
        new_head = Node(new_value)           #Crea un nuevo nodo que tomará la cabeza de la lista
        new_head.set_next_node(self.head_node) #asigna el link de la cabeza nueva a la antigua cabeza
        self.head_node = new_head
    
    def string_list(self):
        the_string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:         #Si curent value no está vacio:
                the_string_list += str(current_node.get_value()) + "\n" #Agrega al string el valor de current value y se salta un renglón
            current_node = current_node.get_next_node()          #Cambia al siguiente nodo
        return the_string_list
    
    def remove_node(self,value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node



