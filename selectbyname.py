bl_info = {
    "name": "Select by name",
    "author": "RamenSlayer",
    "version": (1, 0),
    "blender": (2, 91, 2),
    "location": "View3D > Select",
    "description": "Select multiple objects with similar name with one button.",
    "category": "Object",
}

import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)

from bpy.props import (StringProperty)

#function for checking if all words in a list are in a string
def isitin(keywords, searched):
    truthcount=0
    for word in keywords:
        if word.lower() in searched.lower():
            truthcount+=1
    if truthcount==len(keywords):
        return True
    else:
        return False

class OBJECT_OT_namedselect(Operator):
    bl_label = "Select by name"
    bl_idname = "object.named_select"
    bl_description = "Selects all object with a certain name (also unhides them)"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}
    
    selectnames: bpy.props.StringProperty(
        name = "Names",
        default = "Cube",
        description = "String used for identifying what objects should be selected (if more than one write a space between words)"
        )    

    def execute(self, context):
        select_keywords=self.selectnames.split()
        bpy.ops.object.select_all(action='DESELECT')
        for object in bpy.data.objects:
            if isitin(select_keywords, object.name.lower()):
                object.hide_set(False)
                object.select_set(True)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_namedselect.bl_idname)
    
def register():
    bpy.utils.register_class(OBJECT_OT_namedselect)
    bpy.types.VIEW3D_MT_object_select.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_namedselect)
    bpy.types.VIEW3D_MT_select_object.remove(menu_func)
    
if __name__ == "__main__":
    register()
