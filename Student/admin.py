from django.contrib import admin

# Register your models here.
from .models import Student

class  StudentModelAdmin(admin.ModelAdmin):
	list_display= ["name","username","rollno","batch","current_CGPA"]
	list_display_links = ["rollno"]
	list_editable =["current_CGPA"]
	list_filter = ["current_CGPA","rollno","batch"]
	search_fields = ["rollno","name","batch"]

	class Meta:
		model = Student
	
		
admin.site.register(Student,StudentModelAdmin)