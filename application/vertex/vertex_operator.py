import bpy
import bmesh


# ------------------------
# Operator
# ------------------------
class VERTEX_OT_print_vertex_location(bpy.types.Operator):
    bl_idname = "mesh.print_vertex_location"
    bl_label = "Print Vertex Location"

    use_world: bpy.props.BoolProperty(
        name="World Space",
        default=True
    )

    only_selected: bpy.props.BoolProperty(
        name="Only Selected",
        default=False
    )

    def execute(self, context):
        obj = context.object

        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "Select a mesh object")
            return {'CANCELLED'}

        print("\n=== Vertex Coordinates ===")

        if context.mode == 'EDIT_MESH':
            bm = bmesh.from_edit_mesh(obj.data)

            for v in bm.verts:
                if self.only_selected and not v.select:
                    continue

                co = v.co
                if self.use_world:
                    co = obj.matrix_world @ co

                print(f"{v.index}: {co}")

        else:
            for v in obj.data.vertices:
                if self.only_selected:
                    continue

                co = v.co
                if self.use_world:
                    co = obj.matrix_world @ co

                print(f"{v.index}: {co}")

        self.report({'INFO'}, "Printed to console")
        return {'FINISHED'}

classes = (
    VERTEX_OT_print_vertex_location,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    print("Vertex 로케이션 출력기 Domain이 등록 되었습니다.")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print("Vertex 로케이션 출력기 Domain이 해제 되었습니다.")