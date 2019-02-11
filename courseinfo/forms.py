from django import forms

from courseinfo.models import *


class InstructorForm(forms.ModelForm):
    class Meta:

        model = Instructor
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()


class SectionForm(forms.ModelForm):
    class Meta:

        model = Section
        fields = '__all__'

    def clean_section_name(self):
        return self.cleaned_data['section_name'].strip()


class CourseForm(forms.ModelForm):
    class Meta:

        model = Course
        fields = '__all__'

    def clean_course_name(self):
        return self.cleaned_data['course_name'].strip()

    def clean_course_number(self):
        return self.cleaned_data['course_number'].strip()


class SemesterForm(forms.ModelForm):
    class Meta:

        model = Semester
        fields = '__all__'

    def clean_semester_name(self):
        return self.cleaned_data['semester_name'].strip()


class StudentForm(forms.ModelForm):
    class Meta:

        model = Student
        fields = '__all__'

    def clean_student_first_name(self):
        return self.cleaned_data['student_first_name'].strip()

    def clean_student_last_name(self):
        return self.cleaned_data['student_last_name'].strip()

    def clean_student_nickname(self):
        return self.cleaned_data['student_nickname'].strip()


class RegistrationForm(forms.ModelForm):
    class Meta:

        model = Registration
        fields = '__all__'
