from django.urls import path
from.import views

urlpatterns = [
    path("",views.students_detail,name="students_detail"),
    path("insert",views.student_insert,name="student_insert"),
    path("save",views.insert_save,name="insert_save"),
    path("edit/<student_id>",views.student_edit,name="student_edit"),
    path("save/<student_id>",views.student_updated,name="student_updated"),
    path("remove/<student_id>",views.student_delete,name='student_delete'),
    path("<student_id>",views.student_all_detail,name="student_all_detail"),
    
]
