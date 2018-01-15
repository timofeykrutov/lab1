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
    fields = ('teacher_fio', 'teacher_department')
    list_filter = ('teacher_fio', 'teacher_department')
    list_display = ('teacher_fio', 'teacher_department')
    search_fields = ('teacher_fio', 'teacher_department')

class GroupsAdmin(admin.ModelAdmin):
    fields = ('group_number', 'faculty')
    list_filter = ('group_number', 'faculty')
    list_display = ('group_number', 'faculty')
    search_fields = ('group_number', 'faculty')

admin.site.register(Book)
admin.site.register(Writer)

admin.site.register(teachers, TeacherAdmin)
admin.site.register(groups, GroupsAdmin)
admin.site.register(students)
admin.site.register(teacherBMT, TeacherAdminBMT)
admin.site.register(teacherRT, TeacherAdminRT)
admin.site.register(teacherSM, TeacherAdminSM)
admin.site.register(teacherIU, TeacherAdminIU)
# Register your models here.

