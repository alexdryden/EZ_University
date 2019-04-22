from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from courseinfo.forms import *
from courseinfo.utils import PageLinksMixin
from .models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration,
)


class InstructorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    permission_required = 'courseinfo.view_instructor'
    paginate_by = 25
    model = Instructor


class InstructorDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_instructor'

    def get(self, request, pk):
        instructor = get_object_or_404(
            Instructor,
            pk=pk

        )
        section_list = instructor.sections.all()
        return render(request,
                      'courseinfo/instructor_detail.html',
                      {
                'instructor': instructor,
                'section_list': section_list,
            }
                      )


class SectionList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'courseinfo.view_section'
    model = Section


class SectionDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_section'

    def get(self, request, pk):
        section = get_object_or_404(
            Section,
            pk=pk
        )
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registration.all()
        return render(request,
                      'courseinfo/section_detail.html',
                      {
                'section': section,
                'semester': semester,
                'course': course,
                'instructor': instructor,
                'registration_list': registration_list,

            }

                      )


class CourseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'courseinfo.view_course'
    model = Course


class CourseDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_course'

    def get(self, request, pk):
        course = get_object_or_404(
            Course,
            pk=pk

        )
        section_list = course.sections.all()
        return render(request,
                      'courseinfo/course_detail.html',
                      {
                'course': course,
                'section_list': section_list,

            }
                      )


class SemesterList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'courseinfo.view_semester'
    model = Semester


class SemesterDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_semester'

    def get(self, request, pk):
        semester = get_object_or_404(
            Semester,
            pk=pk

        )
        section_list = semester.sections.all()
        return render(request,
                      'courseinfo/semester_detail.html',
                      {
                'semester': semester,
                'section_list': section_list,

            }
                      )


class StudentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    permission_required = 'courseinfo.view_student'
    paginate_by = 25
    model = Student


class StudentDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_student'

    def get(self, request, pk):
        student = get_object_or_404(
            Student,
            pk=pk

        )
        registration_list = student.registration.all()
        return render(request,
                      'courseinfo/student_detail.html',
                      {'student': student,
                       'registration_list': registration_list,}
                      )


class RegistrationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'courseinfo.view_registration'
    model = Registration


class RegistrationDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_registration'

    def get(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk

        )

        return render(request,
                      'courseinfo/registration_detail.html',
                      {'registration': registration}
                      )


class InstructorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'courseinfo.add_instructor'
    form_class = InstructorForm
    model = Instructor


class SectionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'courseinfo.add_section'
    form_class = SectionForm
    model = Section


class CourseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'courseinfo.add_course'
    form_class = CourseForm
    model = Course


class SemesterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'courseinfo.add_semester'
    form_class = SemesterForm
    model = Semester


class StudentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'courseinfo.add_student'
    form_class = StudentForm
    model = Student


class RegistrationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'courseinfo.add_registration'
    form_class = RegistrationForm
    model = Registration


class InstructorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'courseinfo.change_instructor'
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'


class SectionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'courseinfo.change_section'
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'


class CourseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'courseinfo.change_course'
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'


class SemesterUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'courseinfo.change_semester'
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'


class StudentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'courseinfo.change_student'
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'


class RegistrationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'courseinfo.change_registration'
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'


class InstructorDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.delete_instructor'

    def get(self, request, pk):
        instructor = self.get_object(pk)
        sections = instructor.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/instructor_refuse_delete.html',
                {'instructor': instructor,
                 'sections': sections}
            )
        else:
            return render(
                request,
                'courseinfo/instructor_confirm_delete.html',
                {'instructor': instructor}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Instructor,
            pk=pk
        )

    def post(self, request, pk):
        instructor = self.get_object(pk)
        instructor.delete()
        return redirect('courseinfo_instructor_list_urlpattern')


class SectionDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.delete_section'

    def get(self, request, pk):
        section = self.get_object(pk)
        registrations = section.registration.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/section_refuse_delete.html',
                {'section': section,
                 'registrations': registrations}
            )

        else:
            return render(
                request,
                'courseinfo/section_confirm_delete.html',
                {'section': section}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Section,
            pk=pk
        )

    def post(self, request, pk):
        section = self.get_object(pk)
        section.delete()
        return redirect('courseinfo_section_list_urlpattern')


class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.delete_course'

    def get(self, request, pk):
        course = self.get_object(pk)
        sections = course.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course,
                 'sections': sections}
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Course,
            pk=pk
        )

    def post(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return redirect('courseinfo_course_list_urlpattern')


class SemesterDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.delete_semester'

    def get(self, request, pk):
        semester = self.get_object(pk)
        sections = semester.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/semester_refuse_delete.html',
                {'semester': semester,
                 'sections': sections}
            )
        else:
            return render(
                request,
                'courseinfo/semester_confirm_delete.html',
                {'semester': semester}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Semester,
            pk=pk
        )

    def post(self, request, pk):
        semester = self.get_object(pk)
        semester.delete()
        return redirect('courseinfo_semester_list_urlpattern')


class StudentDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.delete_student'

    def get(self, request, pk):
        student = self.get_object(pk)
        registrations = student.registration.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/student_refuse_delete.html',
                {'student': student,
                 'registrations': registrations}
            )
        else:
            return render(
                request,
                'courseinfo/student_confirm_delete.html',
                {'student': student}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Student,
            pk=pk
        )

    def post(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return redirect('courseinfo_student_list_urlpattern')


class RegistrationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'courseinfo.delete_registration'
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')
