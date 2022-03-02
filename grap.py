from graphviz import Graph
dot = Graph('Ast','png')
dot.format = 'png'
dot.attr(splines = 'false')
dot.node_attr.update(shape = 'circle')
dot.node_attr.update(color = 'blue')