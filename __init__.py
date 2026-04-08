import bpy
from .application.vertex import vertex_pannel

modules = [
    vertex_pannel
]

def register():
    for module in modules:
        module.register()

def unregister():
    for module in reversed(modules):
        module.unregister()
