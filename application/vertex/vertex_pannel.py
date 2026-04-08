import bpy
from . import vertex_operator

# ------------------------
# Pannel
# ------------------------
class VIEW3D_PT_vertex_inspector(bpy.types.Panel):
    bl_label = "Vertex 좌표 출력기"
    bl_idname = "VIEW3D_PT_vertex_inspector"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Vertex'

    def draw(self, context):
        layout = self.layout

        layout.label(text="Vertex Tools")

        col = layout.column(align=True)

        op = col.operator("mesh.print_vertex_location", text="모든 Vertex 좌표 출력하기")
        op.use_world = True
        op.only_selected = False

        op = col.operator("mesh.print_vertex_location", text="선택한 Vertex만 (Edit Mode)")
        op.use_world = True
        op.only_selected = True

        layout.separator()

        layout.label(text="팁:")
        layout.label(text="- Edit Mode에서 사용하세요.")
        layout.label(text="- Window → Toggle System Console에서 확인합니다.")

classes = (
    VIEW3D_PT_vertex_inspector,
)

def register():
    vertex_operator.register()
    for cls in classes:
        bpy.utils.register_class(cls)
    print("Vertex 로케이션 출력기 UI가 등록 되었습니다.")

def unregister():
    vertex_operator.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print("Vertex 로케이션 출력기 UI가 해제 되었습니다.")