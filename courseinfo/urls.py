from django.urls import path

from courseinfo.views import *

# dict structure: key is 2-tuple (descriptivePart, logicPart), value is View
urlpatterns_dict = {('instructor_list',''): InstructorList,
                    ('section_list',''): SectionList,
                    ('course_list',''): CourseList,
                    ('semester_list',''): SemesterList,
                    ('student_list',''): StudentList,
                    ('registration_list',''): RegistrationList,
                    ('instructor_detail', '<int:pk>'): InstructorDetail,
                    ('section_detail', '<int:pk>'): SectionDetail,
                    ('course_detail', '<int:pk>'): CourseDetail,
                    ('semester_detail', '<int:pk>'): SemesterDetail,
                    ('student_detail', '<int:pk>'): StudentDetail,
                    ('registration_detail', '<int:pk>'): RegistrationDetail,
                    ('instructor_create', ''): InstructorCreate,
                    ('section_create', ''): SectionCreate,
                    ('course_create', ''): CourseCreate,
                    ('semester_create', ''): SemesterCreate,
                    ('student_create', ''): StudentCreate,
                    ('registration_create', ''): RegistrationCreate,
                    ('instructor_update', '/<int:pk>'): InstructorUpdate,
                    ('section_update', '/<int:pk>'): SectionUpdate,
                    ('course_update', '/<int:pk>'): CourseUpdate,
                    ('semester_update', '/<int:pk>'): SemesterUpdate,
                    ('student_update', '/<int:pk>'): StudentUpdate,
                    ('registration_update', '/<int:pk>'): RegistrationUpdate,
                    ('course_delete', '/<int:pk>'): CourseDelete,
                    ('instructor_delete', '/<int:pk>'): InstructorDelete,
                    ('section_delete', '/<int:pk>'): SectionDelete,
                    ('student_delete', '/<int:pk>'): StudentDelete,
                    ('registration_delete', '/<int:pk>'): RegistrationDelete,
                    ('semester_delete', '/<int:pk>'): SemesterDelete,

                    }

urlpatterns = [path(key[0]+key[1] + '/',
                    value.as_view(),
                    name='courseinfo_' + key[0] + '_urlpattern')
               for key, value in urlpatterns_dict.items()]

