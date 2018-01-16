from django.contrib import admin
from.models import *

class TeacherAdminIU(admin.ModelAdmin):
    fields = ('teacher_fio', 'teacher_department', 'teacher_f')
    list_filter = ('teacher_fio', 'teacher_department', 'teacher_f' )
    list_display = ('teacher_fio', 'teacher_department', 'teacher_f')
    search_fields = ('teacher_fio', 'teacher_department', 'teacher_f')
    list_per_page = 10

class TeacherAdminRT(admin.ModelAdmin):
    fields = ('teacher_fio', 'teacher_department')
    list_filter = ('teacher_fio', 'teacher_department')
    list_display = ('teacher_fio', 'teacher_department')
    search_fields = ('teacher_fio', 'teacher_department')
    list_per_page = 10

class TeacherAdminSM(admin.ModelAdmin):
    fields = ('teacher_fio', 'teacher_department')
    list_filter = ('teacher_fio', 'teacher_department')
    list_display = ('teacher_fio', 'teacher_department')
    search_fields = ('teacher_fio', 'teacher_department')
    list_per_page = 10

class TeacherAdminBMT(admin.ModelAdmin):
    fields = ('teacher_fio', 'teacher_department')
    list_filter = ('teacher_fio', 'teacher_department')
    list_display = ('teacher_fio', 'teacher_department')
    search_fields = ('teacher_fio', 'teacher_department')
    list_per_page = 10

class TeacherAdmin(admin.ModelAdmin):
    fields = ('teacher_fio', 'teacher_department', 'group_num')
    list_filter = ('teacher_fio', 'teacher_department', ('group_num', admin.RelatedOnlyFieldListFilter))
    list_display = ('teacher_fio', 'teacher_department')
    search_fields = ('teacher_fio', 'teacher_department', 'group_num')

class GroupsAdmin(admin.ModelAdmin):
    fields = ('group_number', 'stud')
    list_filter = ('group_number', 'stud')
    list_display = ('group_number', 'stud')
    search_fields = ('group_number', 'stud')

class StudentsAdmin(admin.ModelAdmin):
    fields = ( 'student_fio', 'group_number')
    list_filter = ( 'student_fio', 'group_number')
    list_display = ( 'student_fio', 'group_number')
    search_fields = ('student_fio', 'group_number')

admin.site.register(Book)
admin.site.register(Writer)

admin.site.register(teachers, TeacherAdmin)
admin.site.register(groups, GroupsAdmin)
admin.site.register(students, StudentsAdmin)
admin.site.register(teacherBMT, TeacherAdminBMT)
admin.site.register(teacherRT, TeacherAdminRT)
admin.site.register(teacherSM, TeacherAdminSM)
admin.site.register(teacherIU, TeacherAdminIU)
# Register your models here.

